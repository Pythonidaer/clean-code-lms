"""Editorial boundaries for Chapter 1. Anchors split preserved text, never summarize it."""
# Each entry starts a slide at an exact, unique source phrase. The first starts at 0.
FLOW = {
'Chapter introduction': [('', 'Learn to recognize and improve code')],
'There Will Be Code': [
('', 'The claim that programming will disappear'),
('We will never be rid of code', 'Code specifies precise requirements'),
('I expect that the level', 'Higher-level languages still need precision'),
('The folks who think', 'Vague intentions are not executable requirements'),
('Indeed, if the discipline', 'Requirements can become executable tests')],
'Bad Code': [
('', 'Why code quality matters'),
('I know of one company', 'A successful product becomes difficult to maintain'),
('Two decades later', 'Accumulated disorder can overwhelm a product'),
('Have you ever been significantly', 'Recognizing the cost of tangled code'),
('Of course you have', 'Why developers leave a mess'),
('We’ve all looked', 'The risk of postponing cleanup')],
'The Total Cost of Owning a Mess': [
('', 'Small changes become expensive'),
('Over time the mess', 'Disorder creates a productivity spiral'),
('But that new staff', 'More people do not automatically fix the design')],
'The Grand Redesign in the Sky': [
('', 'The team asks for a complete redesign'),
('Now the two teams', 'The replacement must chase a moving target'),
('This race can go on', 'The new system can inherit the same problems')],
'Attitude': [
('', 'Recognizing symptoms of code decay'),
('But the fault', 'The author argues for developer responsibility'),
('The managers and marketers', 'Developers contribute to requirements and planning'),
('“But wait!”', 'Communicating risk under deadline pressure'),
('To drive this point home', 'The hand-washing analogy for professional judgment')],
'The Primal Conundrum': [('', 'Keeping code clean is part of moving quickly')],
'The Art of Clean Code?': [
('', 'Recognizing quality is different from creating it'),
('When hand-washing', 'Background to the hand-washing analogy'),
('Writing clean code requires', 'Developing judgment through small techniques'),
('A programmer without', 'Judgment guides behavior-preserving changes')],
'What Is Clean Code?': [('', 'Several perspectives on clean code')],
'Bjarne Stroustrup': [
('', 'Bjarne Stroustrup: focused and carefully implemented code'),
('Bjarne uses the word', 'Elegance includes readability and efficiency'),
('Bad code tempts', 'Neglect can encourage further neglect'),
('Bjarne also mentions that error', 'Complete handling requires attention to detail'),
('Bjarne closes', 'Clean code has a focused purpose')],
'Grady Booch': [
('', 'Grady Booch: make the design intent clear'),
('Grady makes', 'Readable code explains the problem and solution'),
('I find Grady’s', 'Use decisive abstractions without unnecessary detail')],
'Dave Thomas': [
('', 'Dave Thomas: code others can read and enhance'),
('Big Dave shares', 'Readability and changeability are different'),
('Dave ties', 'Tests support confidence in changes'),
('Dave uses the word', 'Prefer small, human-readable implementations')],
'Michael Feathers': [('', 'Michael Feathers: care is visible in the details'), ('One word: care.', 'Care means maintaining simplicity and order')],
'Ron Jeffries': [
('', 'Ron Jeffries: priorities for simple code'),
('Of these, I focus', 'Duplication can reveal an unexpressed idea'),
('I also look at whether', 'Separate responsibilities to reveal intent'),
('There is, however', 'Recognize recurring operations'),
('When I find that happening', 'A small abstraction preserves room to change'),
('In addition, the collection', 'An abstraction can clarify what is really needed')],
'Ward Cunningham': [
('', 'Ward Cunningham: code should meet the reader’s expectations'),
('“. . . pretty much', 'Surprising code makes understanding harder'),
('Ward expects', 'Each module prepares the reader for the next'),
('And what about Ward’s', 'Express the problem clearly in the language')],
'Schools of Thought': [
('', 'This book represents one school of thought'),
('Martial artists', 'Different schools develop different techniques'),
('Students of these approaches', 'Learning can extend across schools'),
('None of these different', 'A school’s conventions are not universal truth'),
('We are willing to claim', 'Consider other professional perspectives'),
('Indeed, many of the recommendations', 'Evaluate recommendations without assuming final authority')],
'We Are Authors': [
('', 'Write code for the people who will read it'),
('You might ask', 'Editing includes a great deal of reading'),
('Bob enters', 'Following an edit session: finding context'),
('Ooops,', 'Following an edit session: checking callers'),
('. . . You get the drift', 'Easier reading supports easier writing'),
('There is no escape', 'Surrounding code affects the next change')],
'The Boy Scout Rule': [
('', 'Leave the code cleaner than you found it'),
('If we all checked-in', 'Small improvements can accumulate over time')],
'Prequel and Principles': [('', 'How this book connects to design principles')],
'Conclusion': [
('', 'Reading provides tools; practice develops judgment'),
('Just like a book on art', 'Learning continues through examples and practice')],
}

# Exact author-introduction boundaries inside “What Is Clean Code?”.
PERSPECTIVES = [
('Bjarne Stroustrup', 'Bjarne Stroustrup, inventor'),
('Grady Booch', 'Grady Booch, author'),
('Dave Thomas', '“Big” Dave Thomas, founder'),
('Michael Feathers', 'Michael Feathers, author'),
('Ron Jeffries', 'Ron Jeffries, author'),
('Ward Cunningham', 'Ward Cunningham, inventor'),
]

def slices(text, entries):
    starts=[0]
    for phrase,_ in entries[1:]:
        assert text.count(phrase)==1, f'Anchor missing or ambiguous: {phrase}'
        starts.append(text.index(phrase))
    assert starts==sorted(starts), 'Editorial boundaries must preserve source order'
    return [(title,text[a:b].strip(),a,b) for (phrase,title),a,b in zip(entries,starts,starts[1:]+[len(text)])]

def build_unit(unit, prefix, deck):
    groups=[];title=unit['title'];blocks=[]
    for block in unit['blocks']:
        if block['kind']=='heading':
            groups.append((title,blocks));title=block['title'];blocks=[]
        else: blocks.append(block)
    groups.append((title,blocks))
    expanded=[]
    for title,blocks in groups:
        text='\n\n'.join(b['body'].replace('../../assets/','assets/') for b in blocks)
        if title=='What Is Clean Code?':
            starts=[0]+[text.index(anchor) for _,anchor in PERSPECTIVES]
            names=[title]+[name for name,_ in PERSPECTIVES]
            expanded.extend((name,text[a:b].strip()) for name,a,b in zip(names,starts,starts[1:]+[len(text)]))
        else: expanded.append((title,text))
    children=[];mapping=[]
    for i,(title,text) in enumerate(expanded,1):
        parts=slices(text,FLOW[title])
        child_id=prefix if len(expanded)==1 else f'{prefix}-part-{i:02}'
        children.append(deck(child_id,title,[(t,b) for t,b,_,_ in parts]))
        for j,(t,b,a,z) in enumerate(parts,1):
            mapping.append(dict(slideId=f'{child_id}-s{j}',title=t,sourceSubheading=title,wordCount=len(b.split()),sourceStart=a,sourceEnd=z))
    result=children[0] if len(children)==1 else dict(id=prefix,type='section',title=unit['title'],children=children)
    return result,mapping
