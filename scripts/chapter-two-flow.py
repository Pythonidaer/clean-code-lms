"""Editorial Chapter 2 boundaries. Source wording and code stay together and ordered."""
import runpy
from pathlib import Path
slices=runpy.run_path(str(Path(__file__).with_name('chapter-one-flow.py')))['slices']
FLOW={
'Introduction':[('', 'Names are part of everyday programming')],
'Use Intention-Revealing Names':[
('', 'A name should explain why it exists'),
('The name `d` reveals', 'Include the quantity and its units'),
('Choosing names that reveal', 'Short code can still hide its purpose'),
('Why is it hard', 'Identify the context the reader has to guess'),
('The answers to these questions', 'Give the game concepts explicit names'),
('Notice that the simplicity', 'Hide representation details behind a meaningful operation')],
'Avoid Disinformation':[
('', 'Avoid names that suggest the wrong concept'),
('Do not refer', 'Do not imply a collection type incorrectly'),
('Beware of using', 'Make important differences easy to see'),
('With modern Java environments', 'Names need to be recognizable in completion lists'),
('A truly awful example', 'Avoid letters that look like numbers'),
('The reader may think', 'Rename the ambiguity instead of changing the font')],
'Make Meaningful Distinctions':[
('', 'Different names should mean different things'),
('Number-series naming', 'Name the source and destination by their roles'),
('Noise words are another', 'Adding Info or Data may not explain a difference'),
('Note that there is nothing', 'A convention is useful when it carries meaning'),
('Noise words are redundant', 'Remove labels that repeat what is already clear'),
('There is an application', 'Similar API names should communicate distinct operations'),
('How are the programmers', 'Help readers choose the right operation')],
'Use Pronounceable Names':[
('', 'Choose names people can discuss aloud'),
('A company I know', 'An abbreviation can become a shared guessing game'),
('New developers had', 'Compare abbreviated names with readable names'),
('Compare with:\n\n```text', 'Readable names make a useful conversation possible')],
'Use Searchable Names':[
('', 'A named concept is easier to find than a number'),
('Likewise, the name', 'Make names searchable across their scope'),
('My personal preference', 'Match the name to how widely it is used'),
('Once again compare', 'An unnamed calculation hides the meaning of its numbers'),
('Compare with:\n\n```text', 'Named constants explain the calculation'),
('Note that `sum`', 'Searchability can be worth a longer expression')],
'Avoid Encodings':[('', 'Avoid making readers decode type or scope')],
'Hungarian Notation':[
('', 'Type encodings addressed older language limitations'),
('The compiler did not', 'Modern type systems reduce the need for encoded names'),
('Java programmers', 'An encoded type can become misleading after a change')],
'Member Prefixes':[
('', 'The author recommends clear names over member prefixes'),
('Besides, people quickly', 'Repeated prefixes can become ignored clutter')],
'Interfaces and Implementations':[
('', 'Name an interface for the role it provides'),
('I don’t want my users', 'The author prefers marking an implementation when needed')],
'Avoid Mental Mapping':[
('', 'Use names readers do not have to translate'),
('However, in most', 'A placeholder name makes readers memorize a mapping'),
('In general programmers', 'Use your understanding to make the code clear to others')],
'Class Names':[('', 'Use nouns for classes and objects')],
'Method Names':[
('', 'Use verbs and meaningful predicate names'),
('When constructors', 'A named factory can explain the construction arguments')],
"Don't Be Cute":[('', 'Choose clarity over an inside joke'),('Cuteness in code', 'Avoid slang that hides the intended operation')],
'Pick One Word per Concept':[
('', 'Use consistent vocabulary for the same operation'),
('Modern editing environments', 'Method names need to stand on their own'),
('Likewise, it’s confusing', 'Role names should express real distinctions')],
"Don't Pun":[
('', 'Do not reuse a term for different meanings'),
('Let’s say we have', 'Adding values and appending an item are different ideas'),
('Our goal, as authors', 'Make the meaning clear rather than requiring study')],
'Use Solution Domain Names':[
('', 'Use technical terms your programming readers know'),
('The name `AccountVisitor`', 'Known technical names can communicate a useful concept')],
'Use Problem Domain Names':[('', 'Use domain vocabulary for domain concepts')],
'Add Meaningful Context':[
('', 'Give names an understandable surrounding context'),
('Imagine that you have', 'An isolated state value needs an address context'),
('You can add context', 'A meaningful structure can provide the context'),
('Consider the method', 'Listing 2-1: context must be inferred from the function'),
('The function is a bit', 'Give the message parts a clear shared context'),
('**Listing 2-2', 'Listing 2-2: named message responsibilities')],
"Don't Add Gratuitous Context":[
('', 'A product prefix can make names harder to find'),
('Likewise, say you invented', 'Do not attach a reusable concept to an irrelevant product'),
('Shorter names are generally', 'Use only the context needed to be precise')],
'Final Words':[
('', 'Good naming depends on shared understanding'),
('Most of the time', 'Tools help readers focus on meaning'),
('You will probably', 'Improve names with help from refactoring tools')],
}
# Nested groups expose genuine source subheadings and the two extended examples.
GROUPS={
'Use Intention-Revealing Names':[(0,2,'Meaning and units'),(2,4,'Reading the unclear example'),(4,6,'Making the game concepts explicit')],
'Add Meaningful Context':[(0,3,'Providing context'),(3,4,'Listing 2-1 — Unclear context'),(4,6,'Listing 2-2 — Explicit context')],
}

def build_unit(unit,prefix,deck):
    groups=[];title=unit['title'];blocks=[]
    for b in unit['blocks']:
        if b['kind']=='heading':groups.append((title,blocks));title=b['title'];blocks=[]
        else:blocks.append(b)
    groups.append((title,blocks))
    children=[];mapping=[]
    for g,(title,blocks) in enumerate(groups,1):
        text='\n\n'.join(b['body'].replace('../../assets/','assets/') for b in blocks).replace('scope\n\n[N5].','scope [N5].')
        parts=slices(text,FLOW[title])
        partitions=GROUPS.get(title,[(0,len(parts),title)])
        for a,z,name in partitions:
            child_id=prefix if len(groups)==1 and len(partitions)==1 else f'{prefix}-part-{len(children)+1:02}'
            children.append(deck(child_id,name,[(t,b) for t,b,_,_ in parts[a:z]]))
            for j,(t,b,start,end) in enumerate(parts[a:z],1):
                mapping.append(dict(slideId=f'{child_id}-s{j}',title=t,sourceSubheading=title,wordCount=len(b.split()),proseWordCount=len(__import__('re').sub(r'```[^\n]*\n[\s\S]*?\n```','',b).split()),sourceStart=start,sourceEnd=end))
    return (children[0] if len(children)==1 else dict(id=prefix,type='section',title=unit['title'],children=children)),mapping
