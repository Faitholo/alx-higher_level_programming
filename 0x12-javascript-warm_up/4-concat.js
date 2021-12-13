#!/usr/bin/node
const array = process.argv.slice(2);
if (array[0] === undefined && array[1] === undefined) {
  console.log('undefined is undefined');
} else if (array[0] !== undefined && array[1] !== undefined) {
  console.log(array[0] + ' is ' + array[1]);
} else if (array[0] !== undefined && array[1] === undefined) {
  console.log(array[0] + ' is undefined');
} else if (array[0] === undefined && array[1] !== undefined) {
  console.log('undefined is ' + array[1]);
}
