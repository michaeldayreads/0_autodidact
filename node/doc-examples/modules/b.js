console.log('b starting');
exports.done = false;
const a = require('./a.js');
console.log('in b, a.done = %j', a.done);
console.log('The above value is false because b was given an unfinished copy of a.');
exports.done = true;
console.log('b done');
