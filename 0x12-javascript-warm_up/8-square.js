#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  let i, j, string;
  for (i = 0; i < x; i++) {
    string = '';
    for (j = 0; j < x; j++) {
      string += 'X';
    }
    console.log(string);
  }
}
