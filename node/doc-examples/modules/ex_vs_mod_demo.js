const test = require('./exports_vs_module.js');

// the line below does not work
var myTest = test.borked('Patia');
myTest.deeper();
var myTest2 = test.works('Patia');
myTest2.deeper();


