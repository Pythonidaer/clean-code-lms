"""Build the LMS from verified chapter units and separately authored study material."""
from pathlib import Path
import hashlib,json,random,re,runpy

ROOT=Path(__file__).resolve().parents[1]
source=json.loads((ROOT/'docs/chapter-units.json').read_text())
study=runpy.run_path(str(ROOT/'scripts/study-material.py'))
material=study['CHAPTERS'];final=study['FINAL']
runpy.run_path(str(ROOT/'scripts/remaining-study-material.py'))['apply'](material)
prior=json.loads((ROOT/'course.json').read_text())
sections=[];coverage=[];chapter_one_mapping=[];chapter_two_mapping=[];chapter_three_mapping=[];remaining_mapping=[]
cleaner=runpy.run_path(str(ROOT/"scripts/clean-source.py"));cleanup_audit=[]
flow=runpy.run_path(str(ROOT/"scripts/chapter-one-flow.py"))
flow_two=runpy.run_path(str(ROOT/"scripts/chapter-two-flow.py"))
flow_three=runpy.run_path(str(ROOT/"scripts/chapter-three-flow.py"))
remaining_flow=runpy.run_path(str(ROOT/"scripts/remaining-reading-flow.py"))
def leaf_decks(nodes):
    for node in nodes:
        if node["type"]=="section":yield from leaf_decks(node["children"])
        else:yield node

def slug(s):return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
def deck(id,title,pairs,optional=False):
    return dict(id=id,type='slides',title=title,optional=optional,slides=[dict(id=f'{id}-s{i}',title=t,body=b) for i,(t,b) in enumerate(pairs,1)])
def questions(id,qs):
    result=[]
    for i,(prompt,options,answer,explanation) in enumerate(qs,1):
        right=options[answer];options=list(options)
        random.Random(f'{id}-q{i}').shuffle(options)
        result.append(dict(id=f'{id}-q{i}',prompt=prompt,options=options,answer=options.index(right),explanation=explanation))
    return result

def split_code(body,limit=48):
    match=re.fullmatch(r'```(\w*)\n([\s\S]*)\n```',body)
    assert match, 'Expected a fenced source listing'
    language,code=match.groups();lines=code.split('\n')
    groups=[];current=[];length=0
    for line in lines:
        if current and (len(current)>=limit or length+len(line)>2600):
            groups.append(current);current=[];length=0
        current.append(line);length+=len(line)+1
    if current:groups.append(current)
    return [f'```{language}\n'+ '\n'.join(g)+'\n```' for g in groups]

def prose_parts(body,limit=2200):
    # Split at paragraphs/sentences, never inside an inline-code span.
    paras=body.split('\n\n');pieces=[]
    for para in paras:
        if len(para)<=limit:pieces.append(para);continue
        sentences=re.split(r'(?<=[.!?])\s+(?=[A-Z“])',para);current=''
        for sentence in sentences:
            if current and len(current)+len(sentence)>limit:pieces.append(current);current=''
            current+=(' ' if current else '')+sentence
        if current:pieces.append(current)
    return pieces

def unit_slides(unit):
    slides=[];current=[];length=0;topic=unit['title'];listing=None
    def flush():
        nonlocal current,length
        if current:slides.append((topic,'\n\n'.join(current)));current=[];length=0
    for block in unit['blocks']:
        if block['kind']=='heading':
            flush();topic=block['title'];continue
        body=block['body'].replace('../../assets/','assets/')
        if block['kind']=='code':
            flush();pieces=split_code(body)
            for i,piece in enumerate(pieces,1):
                code_title=listing or topic
                label=code_title if len(pieces)==1 else f'{code_title} · listing part {i} of {len(pieces)}'
                note='' if len(pieces)==1 else '*Continuation of the same source listing; this fragment is not a standalone program.*\n\n'
                slides.append((label,note+piece))
            listing=None
        elif block['kind']=='listing':
            flush();listing=body.strip('*')
        elif block['kind']=='figure':
            current.append(body);length+=len(body)
        else:
            for piece in prose_parts(body):
                if current and length+len(piece)>2200:flush()
                current.append(piece);length+=len(piece)+2
    flush()
    # Keep short examples beside their explanations instead of making one-line slides.
    combined=[]
    for title,body in slides:
        if combined and combined[-1][0]==title and len(combined[-1][1])+len(body)+2<=3200 and 'listing part ' not in title:
            combined[-1]=(title,combined[-1][1]+'\n\n'+body)
        else:combined.append((title,body))
    slides=combined
    # Repeated slide titles receive a stable continuation label, not new invented topics.
    counts={};total={}
    for title,_ in slides:total[title]=total.get(title,0)+1
    result=[]
    for title,body in slides:
        counts[title]=counts.get(title,0)+1
        if total[title]>1:title=f'{title} · {counts[title]} of {total[title]}'
        assert len(body)<20000, 'Runtime would truncate '+title
        result.append((title,body))
    return result

chapters={c['number']:c for c in source}
# Core follows the book order; advanced concurrency is clearly separate and optional.
for number in [*range(1,13),14,17,13]:
    chapter=chapters[number];guide=material[number];optional=number==13
    prefix=f'ch{number:02}';children=[]
    title=f'{number:02} {chapter["title"]}'+(' — Advanced optional' if optional else '')
    intro=[('What you will learn',guide['goal']),('Ideas to look for','\n\n'.join('• '+idea for idea in guide['ideas']))]
    if number==1:intro.append(('Read and apply','Choose a subsection from the outline, read its source explanations and examples, then try the chapter practice before opening its worked check. Quizzes test code-quality decisions, not publication trivia.\n\nThe original book examples are primarily Java. Read them for their design intent; they are historical source excerpts, not runnable demos in this website. A long listing may continue over several slides.\n\nAll content is open by default. Progress and notes stay in this browser. Copy entire course exports the loaded curriculum, including code and quiz answers. The separate index and deferred chapters are not loaded.'))
    if optional:intro.append(('Advanced module','This chapter is optional and is not assessed by the core final quiz. Its lessons and quiz do not block the final assessment when completion gates are enabled. Distinguish Java threads from JavaScript async mechanisms when applying these ideas.'))
    children.append(deck(prefix+'-overview','Chapter overview',intro,optional))
    for index,unit in enumerate(chapter['units'],1):
        if unit['title']=='Bibliography':continue
        if not unit['blocks']:continue
        id=f'{prefix}-topic-{index:02}'
        teaching_unit=cleaner['clean_unit'](unit,number,cleanup_audit)
        pairs=unit_slides(teaching_unit)
        if not pairs:continue
        if number==1:
            node,mapping=flow['build_unit'](teaching_unit,id,deck)
            children.append(node)
            chapter_one_mapping.append(dict(sourceUnit=unit['title'],sourcePath=chapter['sourcePath'],sourcePages=unit['sourcePages'],slides=mapping))
            pairs=[s for d in leaf_decks([node]) for s in d.get('slides',[])]
        elif number==2:
            node,mapping=flow_two['build_unit'](teaching_unit,id,deck)
            children.append(node)
            chapter_two_mapping.append(dict(sourceUnit=unit['title'],sourcePath=chapter['sourcePath'],sourcePages=unit['sourcePages'],slides=mapping))
            pairs=[s for d in leaf_decks([node]) for s in d.get('slides',[])]
        elif number==3:
            node,mapping=flow_three['build_unit'](teaching_unit,id,deck)
            children.append(node)
            chapter_three_mapping.append(dict(sourceUnit=unit['title'],sourcePath=chapter['sourcePath'],sourcePages=unit['sourcePages'],slides=mapping))
            pairs=[s for d in leaf_decks([node]) for s in d.get('slides',[])]
        else:
            node,mapping=remaining_flow['build_unit'](teaching_unit,id,deck,optional,number)
            children.append(node)
            remaining_mapping.append(dict(chapter=number,sourceUnit=unit['title'],sourcePath=chapter['sourcePath'],sourcePages=unit['sourcePages'],slides=mapping))
            pairs=[s for d in leaf_decks([node]) for s in d.get('slides',[])]
        coverage.append(dict(chapter=number,lessonId=id,sourcePath=chapter['sourcePath'],unitTitle=unit['title'],sourcePages=unit['sourcePages'],sourceBlocksSha256=hashlib.sha256(json.dumps(unit['blocks'],sort_keys=True,ensure_ascii=False).encode()).hexdigest(),slides=len(pairs)))
    children.append(deck(prefix+'-practice','Apply the chapter',[('Practice',guide['practice']),('Worked self-check',guide['check'])],optional))
    children.append(dict(id=prefix+'-quiz',type='quiz',title='Check your understanding',skill=chapter['title'],optional=optional,questions=questions(prefix+'-quiz',guide['questions'])))
    sections.append(dict(id=prefix,type='section',title=title,children=children))

resource_decks=[]
for chapter in [1,2]:
    resource_text=(ROOT/f'docs/resources/chapter-{chapter}-notes.md').read_text()
    resource_parts=re.split(r'^## ',resource_text,flags=re.M)[1:]
    resource_slides=[tuple(part.split('\n',1)) for part in resource_parts]
    resource_decks.append(deck(f'resource-ch{chapter:02}-notes',f'Chapter {chapter} — My clean-code notes',[(t,b.strip()) for t,b in resource_slides],True))
sections.append(dict(id='study-resources',type='section',title='Resources',optional=True,children=resource_decks))

course=dict(schemaVersion=1,id='clean-code-core-chapters-v2',title='Clean Code',description='Learn code-quality decisions through the book’s chapters and subsections. Core: Chapters 1–12, 14 and 17. Advanced optional: Chapter 13. Practice and assessments focus on programming concepts.',sections=sections,finalQuiz=dict(id='clean-code-core-final',type='quiz',title='Final assessment',skill='Core code-quality judgment',questions=questions('final',final)),settings=prior['settings'])
(ROOT/'course.json').write_text(json.dumps(course,ensure_ascii=False,indent=2)+'\n')
embedded=json.dumps(course,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
html='<!doctype html>\n<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Clean Code chapters and core programming concepts with practical exercises and assessments."><meta name="theme-color" content="#070b15"><title>Clean Code LMS</title><link rel="stylesheet" href="lms.css"><script src="vendor/marked.umd.js" defer></script><script src="lesson-markdown.js" defer></script><script src="lms-runtime.js" defer></script></head><body class="lms-export-body"><div id="lms-root"></div><script id="lms-course-data" type="application/json">'+embedded+'</script></body></html>\n'
(ROOT/'index.html').write_text(html)
manifest=json.loads((ROOT/'source-manifest.json').read_text());manifest['curriculum']=dict(coreChapters=[*range(1,13),14,17],advancedChapters=[13],deferredChapters=[15,16],lessons=coverage)
(ROOT/'source-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(ROOT/'docs/source-cleanup-audit.json').write_text(json.dumps(cleanup_audit,ensure_ascii=False,indent=2)+'\n')
(ROOT/'docs/chapter-one-slide-map.json').write_text(json.dumps(chapter_one_mapping,ensure_ascii=False,indent=2)+'\n')
(ROOT/'docs/chapter-two-slide-map.json').write_text(json.dumps(chapter_two_mapping,ensure_ascii=False,indent=2)+'\n')
(ROOT/'docs/chapter-three-slide-map.json').write_text(json.dumps(chapter_three_mapping,ensure_ascii=False,indent=2)+'\n')
(ROOT/'docs/remaining-chapters-slide-map.json').write_text(json.dumps(remaining_mapping,ensure_ascii=False,indent=2)+'\n')
leaves=list(leaf_decks(sections))
stats=dict(chapterSections=sum(s['id'].startswith('ch') for s in sections),sourceSubsectionDecks=len(coverage),decks=sum(n['type']=='slides' for n in leaves),slides=sum(len(n.get('slides',[])) for n in leaves),chapterQuizzes=sum(n['type']=='quiz' for n in leaves),chapterQuestions=sum(len(n.get('questions',[])) for n in leaves),finalQuestions=len(final))
(ROOT/'docs/course-stats.json').write_text(json.dumps(stats,indent=2)+'\n')
print(json.dumps(stats))
