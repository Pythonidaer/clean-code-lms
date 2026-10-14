const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const root=path.resolve(__dirname,'..'),read=p=>fs.readFileSync(path.join(root,p),'utf8'),course=JSON.parse(read('course.json'));
assert.deepEqual(JSON.parse(read('index.html').match(/<script id="lms-course-data"[^>]*>(.*?)<\/script>/s)[1]),course);
const context={};vm.createContext(context);vm.runInContext(read('lms-runtime.js')+';globalThis.api=LMS;',context);const model=context.api.validate(course);assert.equal(context.api.ready(model).length,0);
console.log('PASS: course schema, readiness and embedded data parity');
