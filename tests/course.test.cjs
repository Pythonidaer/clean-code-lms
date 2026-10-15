const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'..'),read=p=>fs.readFileSync(path.join(root,p),'utf8'),course=JSON.parse(read('course.json')),manifest=JSON.parse(read('source-manifest.json')),stats=JSON.parse(read('docs/course-stats.json')),source=JSON.parse(read('docs/chapter-units.json'));
const sha=s=>crypto.createHash('sha256').update(s).digest('hex');
assert.deepEqual(JSON.parse(read('index.html').match(/<script id="lms-course-data"[^>]*>(.*?)<\/script>/s)[1]),course);
const context={};vm.createContext(context);vm.runInContext(read('lms-runtime.js')+';globalThis.api=LMS;',context);const model=context.api.validate(course);assert.equal(context.api.ready(model).length,0);
const items=context.api.flatten(model.sections),decks=items.filter(n=>n.type==='slides'),slides=decks.flatMap(d=>d.slides),quizzes=items.filter(n=>n.type==='quiz');
assert.equal(decks.length,stats.decks);assert.equal(slides.length,stats.slides);assert.equal(model.sections.filter(s=>s.id!=='study-resources').length,15);assert.equal(quizzes.length,15);assert.equal(model.finalQuiz.questions.length,20);
assert.deepEqual(manifest.curriculum.coreChapters,[1,2,3,4,5,6,7,8,9,10,11,12,14,17]);assert.deepEqual(manifest.curriculum.advancedChapters,[13]);assert.deepEqual(manifest.curriculum.deferredChapters,[15,16]);
for(const c of manifest.chapters){assert.equal(sha(read(c.sourcePath)),c.sha256);assert.equal(c.unmatchedHeadings.length,0,'TOC headings '+c.chapter);}
assert.equal(manifest.chapters.length,17);assert.equal(manifest.index.includedInLms,false);assert.ok(read(manifest.index.path).includes('PDF page 462'));
assert.ok(!model.sections.some(s=>/^ch(?:15|16)$/.test(s.id)));assert.ok(!items.some(n=>/index|foreword|dedication|publisher|acknowledgment/i.test(n.title)));
const cleaned=JSON.parse(require('node:child_process').execFileSync('python3',['-c',"import json,runpy; s=json.load(open('docs/chapter-units.json')); f=runpy.run_path('scripts/clean-source.py')['clean_unit']; print(json.dumps([{**c,'units':[f(u,c['number']) for u in c['units']]} for c in s]))"],{cwd:root,encoding:'utf8',maxBuffer:5000000}));
const normalize=s=>s.replace(/\s+/g,' ').trim();
for(const chapter of cleaned.filter(c=>c.status!=='deferred')){
 const actual=manifest.curriculum.lessons.filter(l=>l.chapter===chapter.number);
 const wanted=chapter.units.filter(u=>u.title!=='Bibliography'&&u.blocks.length);
 assert.equal(actual.length,wanted.length,'Every source subsection '+chapter.number);
 for(let i=0;i<wanted.length;i++){
  const unit=wanted[i],entry=actual[i],node=(function find(ns){for(const n of ns){if(n.id===entry.lessonId)return n;if(n.children){const found=find(n.children);if(found)return found;}}})(model.sections),ds=node.type==='section'?context.api.flatten(node.children):[node],d={slides:ds.flatMap(n=>n.slides||[])};assert.equal(entry.unitTitle,unit.title);
  const body=d.slides.map(s=>s.body).join('\n\n');
  for(const b of unit.blocks){
   if(b.kind==='heading')assert.ok([1,2,3].includes(chapter.number)?ds.some(n=>n.title===b.title):d.slides.some(s=>s.title.startsWith(b.title)),'Subheading '+b.title);
   if(b.kind==='prose')assert.ok(normalize(body).includes(normalize(b.body)),'Clean teaching prose '+entry.lessonId);
   if(b.kind==='listing')assert.ok(d.slides.some(s=>s.title.startsWith(b.body.replace(/^\*\*|\*\*$/g,''))||s.body.includes(b.body)),'Listing label '+b.body);
   if(b.kind==='code')for(const line of b.body.split('\n').slice(1,-1).filter(l=>l.trim()))assert.ok(body.includes(line),'Code line '+entry.lessonId);
   if(b.kind==='figure')assert.ok(body.includes(b.body.replace('../../assets/','assets/')),'Figure '+entry.lessonId);
  }
 }
}

const pilotMap=JSON.parse(read('docs/chapter-one-slide-map.json'));
for(const unit of cleaned[0].units.filter(u=>u.title!=='Bibliography')){
 const mapping=pilotMap.find(m=>m.sourceUnit===unit.title);
 const actual=mapping.slides.map(m=>{const slide=slides.find(s=>s.id===m.slideId);assert.ok(slide,m.slideId);assert.equal(slide.title,m.title);assert.equal(slide.body.split(/\s+/).length,m.wordCount);assert.ok(m.wordCount<=150,'Chapter 1 reading budget '+m.slideId);return slide.body;}).join('\n\n');
 const expected=unit.blocks.filter(b=>b.kind!=='heading').map(b=>b.body.replace('../../assets/','assets/')).join('\n\n');
 assert.equal(normalize(actual),normalize(expected),'Exact ordered source coverage '+unit.title);
}


const chapterOne=decks.filter(d=>d.id.startsWith('ch01-')).flatMap(d=>d.slides).map(s=>s.body).join('\n\n');
for(const artifact of ['Patterns.1','time?2','windows.3','programming.4','found it.5','1. [Beck07]','4. [Knuth92]','We\n\nare','MacBook®\n\nprovides','give\n\nthe reader','goes\n\nbeyond'])assert.ok(!chapterOne.includes(artifact),'PDF artifact removed '+artifact);
for(const phrase of ['a working mess is better than nothing','We are deeply complicit','MacBook® provides','give the reader','Expressiveness goes beyond names','When hand-washing was first recommended'])assert.ok(normalize(chapterOne).includes(phrase),'Repaired reading '+phrase);
// Verify meaningful numbers/lists and code are never removed by citation cleanup.
const chapterTwo=decks.filter(d=>d.id.startsWith('ch02-')).flatMap(d=>d.slides).map(s=>s.body).join('\n\n');
assert.ok(chapterTwo.includes('1. What kinds of things'));assert.ok(chapterTwo.includes('a1, a2'));
const allText=slides.map(s=>s.body).join('\n\n');assert.ok(allText.includes('EJB2'));assert.ok(allText.includes('base64'));

for(const s of slides){assert.ok(s.body.length<20000,'No runtime truncation '+s.id);assert.equal((s.body.match(/^```/gm)||[]).length%2,0,'Balanced fences '+s.id);}
const prompts=new Set(quizzes.flatMap(q=>q.questions.map(q=>q.prompt)));
for(const q of model.finalQuiz.questions)assert.ok(!prompts.has(q.prompt),'Independent final prompt');
for(const qz of [...quizzes,model.finalQuiz])for(const q of qz.questions){assert.ok(q.answer>=0&&q.answer<q.options.length);assert.ok(q.explanation);assert.equal(new Set(q.options).size,q.options.length);assert.ok(!/dedication|publisher|ISBN|cover image|foreword/i.test(q.prompt),'Concepts only');}
assert.ok(model.sections.find(s=>s.id==='ch13').children.every(n=>n.optional),'Advanced chapter optional');assert.ok(model.sections.filter(s=>s.id!=='ch13'&&s.id!=='study-resources').every(s=>s.children.every(n=>!n.optional)),'Core required');
const counts=[0,0,0];for(const q of model.finalQuiz.questions)counts[q.answer]++;assert.ok(counts.every(n=>n>=3),'No fixed correct-answer position');
const rgb=h=>h.slice(1).match(/../g).map(x=>parseInt(x,16)/255),lum=c=>c.map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4).reduce((a,v,i)=>a+v*[.2126,.7152,.0722][i],0),contrast=(a,b)=>{const x=lum(a),y=lum(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05);};
for(const key of ['text','muted','brand'])for(const bg of ['background','surface'])assert.ok(contrast(rgb(model.settings[key]),rgb(model.settings[bg]))>=4.5,'Text contrast');
console.log('PASS: 17 Markdown chapters; every included TOC subsection, prose block, code line and figure; curriculum exclusions; optional advanced flags; schema, parity, assessments and contrast; '+slides.length+' slides');

const resource=model.sections.at(-1);assert.equal(resource.id,"study-resources");assert.ok(context.api.flatten(resource.children).every(n=>n.optional));assert.ok(decks.find(d=>d.id==="resource-ch01-notes").slides.some(s=>s.title==="Draft rules for future reviews and skills"));

const secondMap=JSON.parse(read('docs/chapter-two-slide-map.json'));
for(const unit of cleaned[1].units){
 const mapping=secondMap.find(m=>m.sourceUnit===unit.title);assert.ok(mapping);
 const actual=mapping.slides.map(m=>{const slide=slides.find(s=>s.id===m.slideId);assert.ok(slide);assert.equal(slide.title,m.title);assert.ok(m.proseWordCount<=150,'Chapter 2 prose budget '+m.slideId);return slide.body;}).join('\n\n');
 const expected=unit.blocks.filter(b=>b.kind!=='heading'&&b.kind!=='listing').map(b=>b.body.replace('../../assets/','assets/')).join('\n\n');
 const actualWithoutLabels=actual.replace(/\*\*Listing 2-[12][^\n]*\*\*/g,'');
 assert.equal(normalize(actualWithoutLabels),normalize(expected),'Ordered Chapter 2 source coverage '+unit.title);
}

const thirdMap=JSON.parse(read('docs/chapter-three-slide-map.json'));
const withoutFences=s=>s.replace(/^```[^\n]*\n?/gm,'');
for(const unit of cleaned[2].units.filter(u=>u.title!=='Bibliography')){
 const mapping=thirdMap.find(m=>m.sourceUnit===unit.title);assert.ok(mapping);
 const actual=mapping.slides.map(m=>{const slide=slides.find(s=>s.id===m.slideId);assert.ok(slide);assert.equal(slide.title,m.title);assert.ok(m.proseWordCount<=150,'Chapter 3 prose budget '+m.slideId);for(const match of slide.body.matchAll(/```[^\n]*\n([\s\S]*?)\n```/g))assert.ok(match[1].split('\n').length<=40,'Chapter 3 code budget '+m.slideId);return slide.body;}).join('\n\n');
 const expected=unit.blocks.filter(b=>b.kind!=='heading').map(b=>b.body.replace('../../assets/','assets/')).join('\n\n');
 assert.equal(normalize(withoutFences(actual)),normalize(withoutFences(expected)),'Ordered Chapter 3 text and code '+unit.title);
}
