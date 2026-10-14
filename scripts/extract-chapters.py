"""Extract chapter Markdown, heading units and provenance from the supplied PDF.

Only PDF pages 32-345 supply chapters. The index is a separate, unloaded file.
Run with a Python environment containing PyMuPDF. Builds need no PDF library.
"""
from pathlib import Path
import collections, hashlib, json, re, sys, unicodedata, subprocess
import fitz

ROOT=Path(__file__).resolve().parents[1]
PDF=Path(sys.argv[1])
doc=fitz.open(PDF)
assert len(doc)==462
toc=[(l,t.replace('Congurable','Configurable'),n) for l,t,n in doc.get_toc()]
chapters=[(int(re.match(r'Chapter (\d+):',t)[1]),t.split(': ',1)[1],n) for level,t,n in toc if level==1 and t.startswith('Chapter ')]
OUT=ROOT/'docs/chapters';OUT.mkdir(parents=True,exist_ok=True)
FIG=ROOT/'assets/figures';FIG.mkdir(parents=True,exist_ok=True)

def norm(s):
    return unicodedata.normalize('NFKC',s).replace('\u00ad','').replace('\x00','')
def key(s):
    return re.sub(r'[^a-z0-9]','',norm(s).lower())
def slug(s):
    return re.sub(r'[^a-z0-9]+','-',norm(s).lower()).strip('-')
def plain_line(line):return norm(''.join(s['text'] for s in line['spans']))
def inline_line(line):
    out=''
    for span in line['spans']:
        t=norm(span['text'])
        out+=('`'+t+'`' if 'Courier' in span['font'] and t.strip() and '`' not in t else t)
    return out
def paragraph(lines):
    result=''
    for line in lines:
        text=inline_line(line).strip()
        if result.endswith('-') and re.match(r'^[a-z]',text):result=result[:-1]+text
        else:result+=(' ' if result else '')+text
    return result

all_units=[];manifest=[];unmatched=[]
for pos,(number,title,start) in enumerate(chapters):
    end=min((chapters[pos+1][2]-1 if pos+1<len(chapters) else 345),345)
    status='advanced' if number==13 else 'deferred' if number in [15,16] else 'core'
    bookmarks=[(level,t,n) for level,t,n in toc if level>1 and start<=n<=end]
    heading_lookup={key(t):(level,t) for level,t,_ in bookmarks}
    blocks=[];found=set()
    for page_no in range(start,end+1):
        page=doc[page_no-1];page_dict=page.get_text('dict')
        # Only teaching figures; chapter-opening artwork/portraits have no figure caption.
        figures=[]
        if re.search(r'Figure\s+\d',page.get_text()):
            for j,info in enumerate(page.get_image_info()):
                box=fitz.Rect(info['bbox'])
                if box.y0<60 or box.y1>615:continue
                relative=f'assets/figures/pdf-{page_no:03}-{j+1}.png'
                page.get_pixmap(matrix=fitz.Matrix(2,2),clip=box,alpha=False).save(ROOT/relative)
                figures.append(dict(kind='figure',body=f'![Source figure on PDF page {page_no}](../../{relative})',page=page_no,y=box.y0,x=box.x0))
        for block in page_dict['blocks']:
            if 'lines' not in block:continue
            if block['bbox'][1]<55 or block['bbox'][1]>615:continue # running headers / bottom page numbers
            lines=block['lines'];text=norm(' '.join(plain_line(l).strip() for l in lines))
            if not text.strip() or 'This page intentionally left blank' in text:continue
            if all(s['size']>=23 for l in lines for s in l['spans']):continue # chapter number/title already represented
            if text.startswith('by ') and block['bbox'][1]<270:continue # authors retained in credit document, not teaching prose
            fonts=[s for l in lines for s in l['spans'] if s['text'].strip()]
            is_code=fonts and all('Courier' in s['font'] for s in fonts)
            heading_text=norm(' '.join(''.join(s['text'] for s in l['spans'] if s['size']>=8).strip() for l in lines))
            heading=heading_lookup.get(key(heading_text)) if heading_text and max((s['size'] for s in fonts),default=0)>=11.5 else None
            if heading:
                level,canonical=heading;found.add(key(canonical));entry=dict(kind='heading',level=level,title=canonical,body=('#'*level)+' '+canonical)
            elif fonts and all(s['size']>=11.5 and 'Bold' in s['font'] for s in fonts) and not is_code:
                # Additional genuine subheadings, including expert definitions.
                entry=dict(kind='heading',level=3,title=text,body='### '+text)
            elif is_code:
                # Source lines already retain leading spaces; do not dehyphenate code.
                code='\n'.join(plain_line(l) for l in lines)
                entry=dict(kind='code',body=code)
            elif text.startswith('Listing ') and all('Bold' in s['font'] for s in fonts):
                entry=dict(kind='listing',body='**'+text+'**')
            else:
                # Preserve paragraph breaks within a PDF block based on baseline gaps.
                groups=[];current=[];prev=None
                for line in lines:
                    if prev is not None and line['bbox'][1]-prev>17:
                        groups.append(current);current=[]
                    current.append(line);prev=line['bbox'][1]
                if current:groups.append(current)
                entry=dict(kind='prose',body='\n\n'.join(paragraph(g) for g in groups))
            entry.update(page=page_no,y=block['bbox'][1],x=block['bbox'][0]);blocks.append(entry)
        blocks+=figures
    blocks.sort(key=lambda b:(b['page'],b['y'],b['x']))
    # Merge adjacent code blocks, including a continuing listing across page boundaries.
    merged=[]
    for b in blocks:
        if b['kind']=='listing' and '(continued)' in b['body']:continue
        if b['kind']=='code' and merged and merged[-1]['kind']=='code':
            merged[-1]['body']+='\n\n'+b['body'];merged[-1]['endPage']=b['page']
        else:merged.append(b)
    blocks=merged
    for b in blocks:
        if b['kind']=='code':b['body']='```text\n'+b['body']+'\n```'
    md='# '+f'Chapter {number} {title}'+'\n\n'+f'Source: Clean Code, PDF pages {start}–{end}. Status: {status}. Original chapter prose and code are extracted below. Running headers, blank notices and chapter-opening artwork are omitted.\n\n'
    md+='\n\n'.join(b['body'] for b in blocks)+'\n'
    filename=f'{number:02}-{slug(title)}.md';path=OUT/filename;path.write_text(md,encoding='utf-8')
    # Lesson boundaries follow the actual level-2 headings in the contents/bookmarks.
    units=[];current=dict(title='Chapter introduction',blocks=[])
    for b in blocks:
        if b['kind']=='heading' and b['level']==2:
            if current['blocks']:units.append(current)
            current=dict(title=b['title'],blocks=[])
        else:current['blocks'].append(b)
    if current['blocks']:units.append(current)
    for unit in units:
        unit['sourcePages']=sorted(set(b['page'] for b in unit['blocks']))
    missing=[dict(level=l,title=t,pdfPage=n) for l,t,n in bookmarks if key(t) not in found]
    unmatched+= [dict(chapter=number,**h) for h in missing]
    all_units.append(dict(number=number,title=title,status=status,startPage=start,endPage=end,sourcePath='docs/chapters/'+filename,units=units))
    manifest.append(dict(chapter=number,title=title,status=status,pdfPages=[start,end],sourcePath='docs/chapters/'+filename,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),tocHeadings=[dict(level=l,title=t,pdfPage=n) for l,t,n in bookmarks],unmatchedHeadings=missing))

# The contents guide the structure, but neither the contents nor index are LMS lessons.
contents='# Table of contents\n\nSource: PDF pages 8–19. Planning reference only.\n\n'
contents+='\n\n'.join('```text\n'+norm(doc[i].get_text(sort=True)).rstrip()+'\n```' for i in range(7,19))+'\n'
(ROOT/'docs/table-of-contents.md').write_text(contents,encoding='utf-8')
index='# Index\n\nSource: PDF pages 444–462. Reference only; excluded from the LMS. Printed references point into the original book.\n\n'
index_pages=norm(subprocess.run(['pdftotext','-layout','-f','444','-l','462',str(PDF),'-'],capture_output=True,text=True,check=True).stdout).split('\f')
if not index_pages[-1].strip():index_pages.pop()
assert len(index_pages)==19
for offset,page in enumerate(index_pages):
    index+=f'## PDF page {444+offset}\n\n```text\n'+page.rstrip()+'\n```\n\n'
(ROOT/'docs/index.md').write_text(index,encoding='utf-8')
(ROOT/'docs/chapter-units.json').write_text(json.dumps(all_units,ensure_ascii=False,indent=2)+'\n')
(ROOT/'source-manifest.json').write_text(json.dumps(dict(source='User supplied clean_code_full.pdf',pdfSha256=hashlib.sha256(PDF.read_bytes()).hexdigest(),pdfPages=462,chapterScope=[32,345],excludedPages=[[1,7],[20,31],[346,443]],tableOfContents=[8,19],index=dict(path='docs/index.md',pdfPages=[444,462],includedInLms=False),chapters=manifest),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(chapters=len(manifest),units=sum(len(c['units']) for c in all_units),unmatchedHeadings=unmatched,figureCount=len(list(FIG.glob('*.png')))),ensure_ascii=False,indent=2))
