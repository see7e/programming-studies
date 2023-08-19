// Implementing hash table in JS

const priceList = new Map();

// add elements
priceList.set('apple', 5);
priceList.set('orange', 7);
priceList.set('banana', '4 EUR');

// retrieve elements
priceList.get('orange'); // 7
priceList.get('banana'); // '4 EUR'

// remove elements
priceList.delete('banana');
priceList.delete('apple');

// Hash table size
priceList.size(); // 1

// Remove all elements
priceList.clear(); // O(1)

// there's another notation that does the same as above
// in Object Notation

let priceList2 = {};

priceList2['apple'] = 5;
priceList2['orange'] = 7;
priceList2['banana'] = '4 EUR';

priceList2['orange'];
priceList2['banana'];

delete priceList2['banana'];
delete priceList2['apple'];

Object.keys(priceList2).length;

priceList2 = {};