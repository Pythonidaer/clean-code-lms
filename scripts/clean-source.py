"""Clean PDF-only artifacts in teaching prose; never edit archived source or code."""
import copy,re
# Audited PDF pages containing numbered footnote blocks. Real numbered teaching lists
# (e.g. Chapter 2 page 49 and Chapter 9 pages 162–163) are not footnotes.
PAGES={1:[34,37,39,40,45],2:[50,51,52,56],3:[63,65,67,68,69,73,78,79],4:[84,96],5:[107,115,118],6:[127,128,129,130],7:[138],8:[147,150],9:[153,158,159,161,162,163],10:[167,169,172,180,181],11:[186,187,188,191,192,193,194,195,196,197,198,199],12:[202,205],13:[208,211,212,213,215,216,217,219,220,221],14:[231,255],17:[316,319,320,321,324,325,327,329,332,337,341,342]}
# Numbered explanatory lists on otherwise footnoted pages are preserved.
LISTS={(9,162,1),(9,162,2),(9,163,1)}

def is_note(ch,b):
    m=re.match(r'^(\d+)\.\s',b.get('body',''))
    return b['kind']=='prose' and m and b['page'] in PAGES.get(ch,[]) and (ch,b['page'],int(m[1])) not in LISTS

def note_parts(body):return re.split(r'\s+(?=\d+\.\s)',body)
def informative(text):
    reference_text=re.sub(r'https?://\S+|www\.\S+|\[[^\]]+\]|\bpp?\.\s*[\d–—-]+|\b[a-z]\.', '',text)
    if not reference_text.strip(' .,;:0123456789–—-'):return False
    if re.fullmatch(r'(?:\[[^\]]+\][.,]?\s*)+(?:pp?\.\s*[\d–—-]+\.?)?',text):return False
    if re.fullmatch(r'(?:[a-z]\.\s*)?(?:https?://|www\.)\S+',text):return False
    if re.match(r'^(?:See\b|Adapted from https?://|Private correspondence\.|Ibid\.|Object Mentor Training Materials\.)',text):return False
    return True

def join_fragments(text):
    # A lowercase continuation after an unfinished phrase is a PDF paragraph break.
    return re.sub(r'(?<=[\w®`,;])\n\n(?=[a-z])',' ',text)

def clean_unit(unit,ch,audit=None):
    result=copy.deepcopy(unit)
    if ch==3 and unit['title']=='Switch Statements':
        unit=copy.deepcopy(unit)
        for i,b in enumerate(unit['blocks']):
            if b['kind']=='prose' and b['body'].endswith('an inheritance'):
                for j in range(i+1,len(unit['blocks'])):
                    tail=unit['blocks'][j]
                    if tail['kind']=='prose' and tail['body'].startswith('relationship so that'):
                        b['body']+=' '+tail['body'];unit['blocks'].pop(j)
                        if audit is not None:audit.append(dict(chapter=ch,page=b['page'],action='rejoin sentence interrupted by listing',original='an inheritance / Listing 3-5 / relationship'))
                        break
                break
    out=[];notes=[];numbers=set()
    for b in unit['blocks']:
        if is_note(ch,b):
            for part in note_parts(b['body']):
                m=re.match(r'^(\d+)\.\s*(.*)',part,re.S)
                if m:
                    numbers.add(int(m[1]));text=m[2].strip()
                    if informative(text):notes.append(dict(b,body=text))
                    if audit is not None:audit.append(dict(chapter=ch,page=b['page'],action='plain explanatory note' if informative(text) else 'remove reference-only footnote',original=part))
    # Inline markers can refer to notes elsewhere in the chapter, not only this unit.
    numbers.update(range(1,23))
    def prose(text,page):
        def marker(m):
            prefix=text[:m.start()];number=int(m[0])
            # Preserve identifiers and version/numeric values, e.g. a1, EJB2,
            # base64 and JUnit 4.3.1. Code and inline-code spans are untouched.
            if prefix.count('`')%2 or re.search(r'(?:\ba|\bEJB|\bbase|\bJunit|\bJUnit)$',prefix):return m[0]
            if re.search(r'\d\.$',prefix):return m[0]
            if number not in numbers:return m[0]
            if audit is not None:audit.append(dict(chapter=ch,page=page,action='remove inline footnote marker',original=text[max(0,m.start()-45):m.end()+20]))
            return ''
        return join_fragments(re.sub(r'(?<=[A-Za-z.!?,”’)])\d{1,2}(?=[\s.,;:]|$)',marker,text))
    def flush_notes():
        out.extend(notes);notes.clear()
    for b in unit['blocks']:
        if is_note(ch,b):
            if ch==1 and b['body'].startswith('2. When hand-washing'):
                out.append(dict(b,body=b['body'][3:]));notes[:]=[n for n in notes if n['body']!=b['body'][3:]]
            continue
        b=copy.deepcopy(b)
        # Explanatory footnotes are collected at the unit end, never inside a sentence.
        if b['kind']=='prose':
            b['body']=prose(b['body'],b['page'])
            if ch==2 and b['body']=='to':
                if audit is not None:audit.append(dict(chapter=ch,page=b['page'],action='clarify comparison connector',original='to'))
                b['body']='Compare with:'
            if out and out[-1]['kind']=='prose' and re.search(r'[\w®`,;]$',out[-1]['body']) and re.match(r'^[a-z]',b['body']):
                out[-1]['body']+=' '+b['body'];continue
        out.append(b)
    flush_notes();result['blocks']=out;return result
