#!/usr/bin/node

let num = process.argv[2];

if (!isNaN(parseInt(process.argv[2]))) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
