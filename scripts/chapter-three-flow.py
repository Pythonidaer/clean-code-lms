"""Chapter 3 semantic reading boundaries, preserving the source and complete listings."""
import runpy,re
from pathlib import Path
slices=runpy.run_path(str(Path(__file__).with_name('chapter-one-flow.py')))['slices']
FLOW={
'Chapter introduction':[
('', 'Functions organize a program'),
('Consider the code', 'Listing 3-1: a function with hidden intent'),
('Do you understand', 'Refactoring can expose the function’s purpose'),
('Unless you are', 'Recognize the intent without knowing every detail'),
('So what is it', 'What helps a function communicate?')],
'Small!':[
('', 'The author argues for very small functions'),
('What this experience', 'The recommendation comes from experience'),
('Nowadays with', 'Screen size is not a useful function-size limit'),
('How short should a function', 'An example from Kent Beck’s Sparkle program'),
('When Kent showed', 'Short functions can form a readable sequence'),
('How short should your functions', 'Listing 3-3: express the operation directly')],
'Blocks and Indenting':[
('', 'Descriptive calls can clarify small blocks'),
('This also implies', 'The author connects small functions with shallow nesting'),
('An open-source', 'Background to the testing example')],
'Do One Thing':[
('', 'A busy function combines different kinds of work'),
('FUNCTIONS SHOULD', 'The one-thing rule needs interpretation'),
('The problem with', 'One operation can contain several steps'),
('So which is it', 'Judge the steps relative to the function’s purpose'),
('If a function does', 'Decompose a concept at the next level down'),
('It should be very clear that Listing 3-1 contains', 'Mixed abstraction levels reveal unrelated work'),
('We could extract', 'Extraction should reveal an idea, not repeat the code')],
'Sections within Functions':[('', 'Internal sections can signal multiple responsibilities')],
'One Level of Abstraction per Function':[
('', 'Keep statements at a consistent level of abstraction'),
('Mixing levels', 'Do not mix essential concepts with implementation details')],
'Reading Code from Top to Bottom: The Stepdown Rule':[
('', 'Let the reader descend through levels of detail'),
('To include the setups and teardowns, we include', 'Read the setup sequence as a hierarchy'),
('It turns out', 'Use the narrative to check abstraction consistency'),
('The LOGO language', 'Why the chapter uses TO paragraphs')],
'Switch Statements':[
('', 'The author’s concern is repeated type-based branching'),
('Consider Listing', 'Listing 3-4: payroll branches on employee type'),
('There are several problems', 'A growing switch can create several reasons to change'),
('But possibly the worst', 'The same branching can spread across operations'),
('The solution to this problem', 'Hide object creation behind a factory'),
('My general rule', 'Read the proposed rule with its qualification'),
('**Listing 3-5', 'Listing 3-5: employee operations and creation')],
'Use Descriptive Names':[
('', 'A focused function is easier to name'),
('Don’t be afraid to make', 'Prefer a descriptive name to an unexplained short one'),
('Don’t be afraid to spend', 'Try names until the design becomes clearer'),
('Be consistent in your names', 'Repeated vocabulary can make the sequence predictable')],
'Function Arguments':[
('', 'The author prefers fewer arguments'),
('Arguments are hard', 'Arguments add context the reader must interpret'),
('When you are reading', 'An argument can expose a lower-level detail'),
('Arguments are even harder', 'More combinations can increase the testing burden'),
('Output arguments', 'Readers usually expect inputs and a return value')],
'Common Monadic Forms':[
('', 'A single argument can support a query or transformation'),
('A somewhat less common', 'An event-style call should communicate its effect'),
('Try to avoid', 'A transformation is clearer when it returns its result')],
'Flag Arguments':[
('', 'A flag can hide a choice between operations'),
('In Listing 3-7', 'A limited refactoring may keep an existing flag')],
'Dyadic Functions':[
('', 'Two arguments can add interpretation work'),
('There are times', 'Related components can naturally belong together'),
('Even obvious dyadic', 'Argument ordering can depend on convention'),
('Dyads aren’t evil', 'Consider alternatives without treating two arguments as forbidden')],
'Triads':[
('', 'Three arguments can make roles harder to follow'),
('On the other hand', 'A tolerance argument can communicate an important distinction')],
'Argument Objects':[
('', 'Group arguments when they express a real concept'),
('Reducing the number', 'A named concept matters more than a smaller count')],
'Argument Lists':[
('', 'A variable-length argument list can represent one group'),
('If the variable arguments', 'Count the conceptual roles in the signature'),
('So all the same rules', 'The author applies the same reasoning to variable arguments')],
'Verbs and Keywords':[
('', 'A function name can explain the argument’s role'),
('This last is', 'Names can make argument ordering explicit'),
('I just finished', 'An example of moving a repeated argument into an object')],
'Have No Side Effects':[
('', 'A hidden effect breaks the promise of a function’s name'),
('Consider, for example', 'Listing 3-6: a password check with an extra effect'),
('The side effect', 'The password check also initializes the session'),
('This side effect creates', 'Hidden effects can create ordering requirements'),
('Temporal couplings', 'Make required ordering visible to the caller')],
'Output Arguments':[
('', 'An argument may ambiguously look like an input'),
('Does this function', 'The caller should not have to guess what changes'),
('This clarifies', 'Checking the declaration interrupts understanding'),
('In the days', 'The chapter proposes placing the operation on the owning object'),
('In general output', 'Make the state being changed clear')],
'Command Query Separation':[
('', 'Separate changing state from asking a question'),
('This function sets', 'A boolean result can obscure whether a call changes state'),
('Imagine this', 'A call inside a condition can be read two ways'),
('The author intended', 'The verb and adjective readings conflict'),
('We could try', 'Separate the command from the existence check')],
'Prefer Exceptions to Returning Error Codes':[
('', 'The chapter links error codes with conditional commands'),
('This does not suffer', 'Immediate error checks can create nested control flow'),
('On the other hand', 'Exceptions can separate error handling from normal work')],
'Extract Try/Catch Blocks':[
('', 'Extract normal work and failure handling into named operations'),
('In the above', 'The example separates deletion from error handling')],
'Error Handling Is One Thing':[('', 'The author treats error handling as a focused responsibility')],
'The Error.java Dependency Magnet':[
('', 'A shared error-code enum can become a dependency'),
('Classes like this', 'Shared error definitions can discourage useful distinctions'),
('When you use exceptions', 'The chapter contrasts exception hierarchies with shared codes')],
"Don't Repeat Yourself":[
('', 'Repeated logic creates repeated maintenance work'),
('It’s not easy', 'Duplication can be hidden among other work'),
('This duplication', 'A shared operation can improve the surrounding story'),
('Duplication may', 'Many design approaches aim to control duplication'),
('Structured programming', 'The author connects reuse with the history of subroutines')],
'Structured Programming':[
('', 'Single entry and exit is a historical discipline'),
('While we are sympathetic', 'The author allows expressive exits in small functions')],
'How Do You Write Functions Like This?':[
('', 'Start with a draft and refine it'),
('When I write functions', 'First drafts can have names and structure worth improving'),
('But I also have', 'Refine the code while keeping the tests passing'),
('In the end', 'Clear functions are the result of revision')],
'Conclusion':[
('', 'Functions help express the language of the system'),
('Master programmers', 'Use the programming language to tell the system’s story'),
('Part of that domain-specific', 'A hierarchy of functions describes the system’s actions'),
('This chapter has', 'Short functions should still fit a clear overall design')],
'SetupTeardownIncluder':[('', 'Listing 3-7 SetupTeardownIncluder.java')],
}

def split_listings(body):
    """Keep listing fragments ordered, at most 40 code lines per slide."""
    chunks=[];current=''
    cursor=0
    for match in re.finditer(r'```([^\n]*)\n([\s\S]*?)\n```',body):
        current+=body[cursor:match.start()];lang,code=match.groups();lines=code.split('\n')
        for i in range(0,len(lines),40):
            piece='```'+lang+'\n'+'\n'.join(lines[i:i+40])+'\n```'
            if i:chunks.append(current.strip());current=''
            current+=piece
        cursor=match.end()
    current+=body[cursor:]
    if current.strip():chunks.append(current.strip())
    return chunks

def build_unit(unit,prefix,deck):
    groups=[];title=unit['title'];blocks=[]
    for b in unit['blocks']:
        if b['kind']=='heading':groups.append((title,blocks));title=b['title'];blocks=[]
        else:blocks.append(b)
    groups.append((title,blocks));children=[];mapping=[]
    for g,(title,blocks) in enumerate(groups,1):
        text='\n\n'.join(b['body'].replace('../../assets/','assets/') for b in blocks)
        parts=slices(text,FLOW[title]);pairs=[]
        child_id=prefix if len(groups)==1 else f'{prefix}-part-{g:02}'
        for t,b,start,end in parts:
            chunks=split_listings(b)
            for i,chunk in enumerate(chunks,1):
                caption=t if len(chunks)==1 else f'{t} · listing continuation {i} of {len(chunks)}'
                pairs.append((caption,chunk))
                mapping.append(dict(slideId=f'{child_id}-s{len(pairs)}',title=caption,sourceSubheading=title,sourceStart=start,sourceEnd=end,listingPart=i,listingParts=len(chunks),proseWordCount=len(re.sub(r'```[^\n]*\n[\s\S]*?\n```','',chunk).split())))
        children.append(deck(child_id,title,pairs))
    return (children[0] if len(children)==1 else dict(id=prefix,type='section',title=unit['title'],children=children)),mapping
