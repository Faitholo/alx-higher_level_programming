#!/usr/bin/node
// script that imports an array and computes a new array

const array = require('./100-data').list;

console.log(array);
let cont = 0;
const map1 = array.map(function (x) {
  return (x * cont++);
});
console.log(map1);
