#!/usr/bin/node
const array = process.argv.slice(2);
let array2 = [];
function sortNumber (a, b) {
  return a - b;
}
if (array[0] === undefined) {
  console.log(0);
} else if (array.length === 1) {
  console.log(0);
} else {
  array2 = array.sort(sortNumber);
  array2.pop();
  console.log(parseInt(array2[array2.length - 1]));
}
