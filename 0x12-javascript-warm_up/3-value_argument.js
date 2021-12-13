#!/usr/bin/node
const array = process.argv.slice(2);
if (array[0] === undefined) {
  console.log('No argument');
} else {
  console.log(array[0]);
}
