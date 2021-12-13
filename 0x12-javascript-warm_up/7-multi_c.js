#!/usr/bin/node
const x = parseInt(process.argv[2]);
let result;
if (isNaN(x)) {
  result = 'Missing number of occurrences';
  console.log(result);
} else {
  result = 'C is fun';
  let i;
  for (i = 0; i < x; i++) {
    console.log(result);
  }
}
