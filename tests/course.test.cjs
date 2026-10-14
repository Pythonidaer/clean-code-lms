const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'..'),read=p=>fs.readFileSync(path.join(root,p),'utf8');
const course=JSON.parse(read('course.json')),html=read('index.html'),manifest=JSON.parse(read('source-manifest.json'));
const embedded=JSON.parse(html.match(/<script id="lms-course-data"[^>]*>(.*?)<\/script>/s)[1]);assert.deepEqual(embedded,course);
const context={};vm.createContext(context);vm.runInContext(read('lms-runtime.js')+';globalThis.api=LMS;',context);
const model=context.api.validate(course);assert.equal(context.api.ready(model).length,0);
const items=context.api.flatten(model.sections),decks=items.filter(n=>n.type==='slides'),slides=decks.flatMap(d=>d.slides);
assert.equal(decks.length,30);assert.equal(slides.length,196);assert.equal(course.sections.length,8);
assert.equal(manifest.guidedCoverage.length,21);
for(const c of manifest.guidedCoverage)assert.ok(decks.some(d=>d.id===c.lessonId),'Guided coverage '+c.lessonId);
for(const s of slides){assert.ok(s.body.length<20000,'No truncation '+s.id);assert.equal((s.body.match(/^```/gm)||[]).length%2,0,'Fences '+s.id);}
// Every single source page is present once, in order, with its exact extracted text.
const source=read(manifest.sourceFile),sha=s=>crypto.createHash('sha256').update(s).digest('hex');assert.equal(sha(source),manifest.sourceSha256);
const parts=[...source.matchAll(/^\[PDF page (\d+)\]\n\n/gm)];assert.equal(parts.length,67);
const archive=model.sections.find(s=>s.id==='source-reference');assert.deepEqual(archive.children.flatMap(d=>d.slides.map(s=>s.id)),Array.from({length:67},(_,i)=>'pdf-page-'+String(i+1).padStart(2,'0')));
parts.forEach((p,i)=>{const page=source.slice(p.index+p[0].length,parts[i+1]?.index??source.length).replace(/\n+$/,'');const entry=manifest.pages[i],deck=decks.find(d=>d.id===entry.lessonId),s=deck.slides.find(s=>s.id===entry.slideId);assert.equal(s.body,'```text\n'+page+'\n```','Full text page '+(i+1));assert.equal(sha(page),entry.textSha256);assert.equal(entry.pdfPage,i+1);});
const quizzes=items.filter(n=>n.type==='quiz');assert.equal(quizzes.length,6);assert.equal(quizzes.reduce((n,q)=>n+q.questions.length,0),23);assert.equal(model.finalQuiz.questions.length,12);
const modulePrompts=new Set(quizzes.flatMap(q=>q.questions.map(q=>q.prompt)));
for(const qz of [...quizzes,model.finalQuiz])for(const q of qz.questions){assert.ok(q.answer>=0&&q.answer<q.options.length);assert.ok(q.explanation);assert.equal(new Set(q.options).size,q.options.length);}
for(const q of model.finalQuiz.questions)assert.ok(!modulePrompts.has(q.prompt),'Independent final question');
assert.ok(!JSON.stringify(course).includes('Design foundations'));assert.ok(!read('lms-runtime.js').includes('Quiz 1 JSON syntax'));
// Contrast for all theme combinations including the mixed active outline surface.
const rgb=h=>h.slice(1).match(/../g).map(x=>parseInt(x,16)/255),lum=c=>c.map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4).reduce((a,v,i)=>a+v*[.2126,.7152,.0722][i],0),contrast=(a,b)=>{const x=lum(a),y=lum(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05);};
const t=model.settings,bgs=[rgb(t.background),rgb(t.surface),rgb(t.brand).map((v,i)=>.14*v+.86*rgb(t.surface)[i])];
for(const key of ['text','muted','brand'])for(const bg of bgs)assert.ok(contrast(rgb(t[key]),bg)>=4.5,'Text contrast '+key);
for(const bg of bgs.slice(0,2))assert.ok(contrast(rgb(t.border),bg)>=3,'Border/focus contrast');
assert.ok(contrast(rgb(t.brand),rgb(context.api.onColor(t.brand)))>=4.5,'Button text contrast');
// Meaningful behavior checks for the original refactoring clinic, including duplicate IDs.
const code=decks.find(d=>d.id==='clinic').slides.at(-1).body.match(/```js\n([\s\S]*?)\n```/)[1],ctx={};vm.createContext(ctx);vm.runInContext(code+';globalThis.lookup=findLessonById;',ctx);
const first={id:'lesson-1'},last={id:'lesson-1'},records=[first,last];assert.equal(ctx.lookup(records,'lesson-1'),first);assert.equal(ctx.lookup(records,'missing'),undefined);assert.equal(ctx.lookup([],'lesson-1'),undefined);assert.deepEqual(records,[first,last]);
console.log('PASS: 67 exact source pages, 21 guided decks, 196 slides, schema, parity, independent assessments, theme contrast and refactoring behavior');
