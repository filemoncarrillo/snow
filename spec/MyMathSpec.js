
var myMath = require('../myMath');

/*
function myMath(){}

myMath.prototype = {
    initialize: function() {
    },
	add: function(a, b) {
		return a + b;
	},
	subtract: function(a, b) {
		return a - b;
	},
    type: 'myMath'
};*/


var my = new myMath();

var myTotal = my.add(1, 2);
//gs.info(myTotal);

var myRest = my.subtract(100, 1);
//gs.info(myRest);

describe('Test Suite for myMath', function() {
	it('Testing add', function() {
		expect(myTotal).toBe(3);
	});
	it('Testing subtract', function() {
		expect(myRest).toBe(99);
	});
});

