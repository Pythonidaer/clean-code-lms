"""Reading-first segmentation for remaining loaded chapters, with source traceability.

Source headings determine navigation. Sentences and discourse transitions determine
prose boundaries; code is never rewritten and long listings have ordered continuations.
"""
import re,copy,runpy
from pathlib import Path
reviewed=runpy.run_path(str(Path(__file__).with_name('remaining-slide-titles.py')))
PROSE_LIMIT=150
TARGET=110
CODE_LIMIT=40
TRANSITION=re.compile(r'^(?:However|On the other hand|For example|Consider|In contrast|Instead|Unfortunately|The problem|There is|There are|This means|But |So |Now |Of course|In general|Notice|Remember|When |If )')

# Short, authored entry titles orient the reader before the preserved source passage.
TITLES={
'Chapter introduction':'What this chapter examines',
'The Purpose of Formatting':'Formatting communicates intent to future readers',
'Team Rules':'Use a shared formatting convention',
'Data Abstraction':'Expose the useful operation rather than storage details',
'Data/Object Anti-Symmetry':'Objects and data structures favor different changes',
'The Law of Demeter':'Limit knowledge of another object’s internal structure',
'Data Transfer Objects':'Transport data without confusing it with domain behavior',
'Use Unchecked Exceptions':'Understand the chapter’s Java exception tradeoff',
'Provide Context with Exceptions':'Explain which operation failed and preserve its cause',
'Define Exception Classes in Terms of a Caller\'s Needs':'Design failure boundaries around the caller’s needs',
'Define the Normal Flow':'Keep expected cases visible in the normal flow',
"Don't Return Null":'Make absence and failure explicit to the caller',
"Don't Pass Null":'Communicate the contract for missing arguments',
'Using Third-Party Code':'Keep external API details inside a useful boundary',
'Exploring and Learning Boundaries':'Learn the behavior your code depends on',
'Learning Tests Are Better Than Free':'Keep checks for the library behavior you rely on',
'Using Code That Does Not Yet Exist':'Define the interface your application needs',
'Clean Boundaries':'Limit how far external changes spread',
'The Three Laws of TDD':'Read the proposed test-driven development cycle',
'Keeping Tests Clean':'Maintain tests as carefully as production code',
'Tests Enable the -ilities':'Tests support confidence when changing a design',
'One Assert per Test':'Consider what each test is trying to communicate',
'Single Concept per Test':'Keep each test focused on one concept',
'Class Organization':'Arrange a class so its structure is understandable',
'Classes Should Be Small!':'Count responsibilities rather than only lines',
'The Single Responsibility Principle':'Identify the reasons a class might change',
'Cohesion':'Keep related state and behavior together',
'Organizing for Change':'Structure the code around likely changes',
'Isolating from Change':'Depend on a useful boundary rather than concrete details',
'Separate Constructing a System from Using It':'Separate object creation from application behavior',
'Dependency Injection':'Supply dependencies through an explicit boundary',
'Scaling Up':'Consider how system boundaries evolve with scale',
'Cross-Cutting Concerns':'Recognize policies that span several components',
'Test Drive the System Architecture':'Keep architectural decisions testable and revisable',
'Optimize Decision Making':'Make decisions where the relevant knowledge exists',
'Use Standards Wisely, When They Add Demonstrable Value':'Evaluate the actual value of a standard',
'Systems Need Domain-Specific Languages':'Use vocabulary that expresses the domain',
'Simple Design Rule 1: Runs All the Tests':'Establish tested behavior before refining the design',
'Simple Design Rules 2–4: Refactoring':'Refine duplication, expression and unnecessary structure',
'No Duplication':'Extract a genuinely shared idea',
'Expressive':'Communicate intent through names and structure',
'Minimal Classes and Methods':'Avoid unnecessary structure after meeting the other goals',
'Why Concurrency?':'Understand why work might run concurrently',
'Myths and Misconceptions':'Check assumptions about concurrency benefits and costs',
'Challenges':'Shared state introduces additional execution possibilities',
'Corollary: Limit the Scope of Data':'Limit access to shared mutable data',
'Corollary: Use Copies of Data':'Consider independent copies instead of shared mutation',
'Corollary: Threads Should Be as Independent as Possible':'Minimize coordination between workers',
'Know Your Library':'Know the actual concurrency guarantees of the library',
'Beware Dependencies Between Synchronized Methods':'A sequence of safe methods may still need coordination',
'Keep Synchronized Sections Small':'Protect the necessary work without widening contention',
'Writing Correct Shut-Down Code Is Hard':'Treat shutdown as a coordination problem',
'Testing Threaded Code':'Look for failures across different execution conditions',
'Treat Spurious Failures as Candidate Threading Issues':'Investigate intermittent failures rather than dismissing them',
'Get Your Nonthreaded Code Working First':'Separate ordinary logic problems from coordination problems',
'Make Your Threaded Code Pluggable':'Keep coordination separate from the ordinary work',
'Make Your Threaded Code Tunable':'Make relevant execution settings adjustable',
'Run with More Threads Than Processors':'Exercise scheduling conditions that may expose faults',
'Run on Different Platforms':'Test assumptions across execution environments',
'Args Implementation':'Read the argument parser before examining its refinement',
'Args: The Rough Draft':'Compare the working draft with the refined design',
'How Did I Do This?':'Refinement proceeds through small checked changes',
'So I Stopped':'Pause feature work when the design becomes difficult to extend',
'On Incrementalism':'Keep the program working while improving its structure',
'String Arguments':'Follow the changes needed to add another argument type',
}

def prose_count(body):return len(re.sub(r'```[^\n]*\n[\s\S]*?\n```','',body).split())
def code_count(body):return sum(len(m[1].split('\n')) for m in re.finditer(r'```[^\n]*\n([\s\S]*?)\n```',body))

def sentences(text):
    # Do not split inside inline code. Preserve its exact contents and all words.
    spans=[m.span() for m in re.finditer(r'`[^`]*`',text)]
    starts=[0]
    for m in re.finditer(r'(?<=[.!?])\s+(?=[A-Z“”‘"(])',text):
        if not any(a<=m.start()<b for a,b in spans):starts.append(m.end())
    return [text[a:b].strip() for a,b in zip(starts,starts[1:]+[len(text)]) if text[a:b].strip()]

def title_for(topic,body,index,listing=None):
    if listing:return listing
    if index==1:return TITLES.get(topic,topic)
    prose=re.sub(r'```[^\n]*\n[\s\S]*?\n```','',body).strip()
    prose=re.sub(r'!\[[^]]*\]\([^)]*\)','',prose).strip()
    if not prose:return topic+' — example'
    lead=sentences(prose)[0]
    lead=re.sub(r'^[*#\s]+|[*#\s]+$','',lead)
    if len(lead)<=145:return lead.rstrip('.')
    # Prefer a complete introductory clause to a mechanically cut word count.
    for match in re.finditer(r'[;:]|, (?:but|and|so|because|which|where)\b',lead):
        if 35<=match.start()<=145:return lead[:match.start()].rstrip(' ,.')
    return topic+' — '+('example and explanation' if '```' in body else 'reasoning and tradeoffs')

def build_unit(unit,prefix,deck,optional=False,chapter=None):
    groups=[];topic=unit['title'];blocks=[]
    for b in unit['blocks']:
        if b['kind']=='heading':groups.append((topic,blocks));topic=b['title'];blocks=[]
        else:blocks.append(b)
    groups.append((topic,blocks));children=[];mapping=[]
    for group_index,(topic,blocks) in enumerate(groups,1):
        if not blocks:continue
        child_id=prefix if len(groups)==1 else f'{prefix}-part-{group_index:02}'
        pairs=[];current=[];refs=[];listing=None;active_listing=None;listing_number=0
        def flush():
            nonlocal current,refs,listing,listing_number
            if not current:return
            body='\n\n'.join(current)
            title=title_for(topic,body,len(pairs)+1,listing)
            if active_listing and '```' in body:
                listing_number+=1
                title=active_listing+f' · listing continuation {listing_number}'
            pairs.append((title,body))
            mapping.append(dict(slideId=f'{child_id}-s{len(pairs)}',title=title,sourceSubheading=topic,sourceBlocks=copy.deepcopy(refs),proseWordCount=prose_count(body),codeLines=code_count(body)))
            current=[];refs=[];listing=None
        def add(text,ref):
            candidate='\n\n'.join(current+[text])
            if current and (prose_count(candidate)>PROSE_LIMIT or code_count(candidate)>CODE_LIMIT):flush()
            if current and refs and ref['kind']=='prose' and refs[-1]['kind']=='prose' and ref.get('block')==refs[-1].get('block') and ref.get('paragraph')==refs[-1].get('paragraph'):
                current[-1]+=' '+text
            else:current.append(text)
            refs.append(ref)
        for block_index,b in enumerate(blocks):
            kind=b['kind'];body=b['body'].replace('../../assets/','assets/')
            ref=dict(block=block_index,page=b.get('page'),kind=kind)
            if kind=='listing':
                flush();active_listing=body.strip('*');listing_number=0;listing=active_listing
                current.append(body);refs.append(ref)
            elif kind=='code':
                match=re.fullmatch(r'```([^\n]*)\n([\s\S]*)\n```',body);assert match
                language,code=match.groups();lines=code.split('\n')
                if len(lines)>CODE_LIMIT and not active_listing:active_listing=topic+' — source listing';listing_number=0
                for a in range(0,len(lines),CODE_LIMIT):
                    if a:flush()
                    add('```'+language+'\n'+'\n'.join(lines[a:a+CODE_LIMIT])+'\n```',dict(ref,lineStart=a+1,lineEnd=min(a+CODE_LIMIT,len(lines))))
            elif kind=='figure':add(body,ref)
            else:
                # A new prose explanation ends an already displayed listing sequence.
                if active_listing and any('```' in p for p in current):
                    flush();active_listing=None;listing_number=0
                for paragraph_index,paragraph in enumerate(body.split('\n\n')):
                    parts=sentences(paragraph)
                    for sentence_index,sentence in enumerate(parts):
                        assert len(sentence.split())<=PROSE_LIMIT, f'Long sentence needs editorial boundary: {unit["title"]}: {sentence[:100]}'
                        if current and prose_count('\n\n'.join(current))>=60 and TRANSITION.match(sentence):flush()
                        add(sentence,dict(ref,paragraph=paragraph_index,sentence=sentence_index))
                        if prose_count('\n\n'.join(current))>=TARGET:flush()
        flush()
        # Repeated fallback titles receive source subsection progress for orientation.
        counts={}
        for title,body in pairs:counts[title]=counts.get(title,0)+1
        seen={};updated=[]
        start=len(mapping)-len(pairs)
        for i,(title,body) in enumerate(pairs):
            seen[title]=seen.get(title,0)+1
            label=title if counts[title]==1 else title+f' · {seen[title]} of {counts[title]}'
            slide_id=f'{child_id}-s{i+1}'
            if topic=='Chapter introduction' and i==0:label=reviewed['INTRO'].get(chapter,label)
            label=reviewed['TITLES'].get(slide_id,label)
            updated.append((label,body));mapping[start+i]['title']=label
        children.append(deck(child_id,topic,updated,optional))
    return (children[0] if len(children)==1 else dict(id=prefix,type='section',title=unit['title'],optional=optional,children=children)),mapping
