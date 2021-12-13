#!/usr/bin/node
const args = process.argv;
let A = parseInt(args[2]);
let B = parseInt(args[3]);
if (typeof A === 'number' && typeof B === 'number') {
  console.log(add(A, B));
} else {
  console.log('NaN');
}

function add (a, b) {
  return (a + b);
}
