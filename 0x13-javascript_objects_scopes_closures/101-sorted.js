#!/usr/bin/node
// Script imports a dictionary of occurrences by user id
// and computes a dictionary of user ids by occurrence.

const { dict } = require('./101-data.js');
const Dictn = {};
for (const N in dict) {
    if (Dictn[dict[N]] === undefined) {
	Dictn[dict[N]] = [];
    }
    Dictn[dict[N]].push(N);
}
console.log(Dictn);
