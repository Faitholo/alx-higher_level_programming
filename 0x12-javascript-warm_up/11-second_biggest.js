#!/usr/bin/node

function second (myArray) {
  if (myArray.length === 2 || myArray.length === 3) { return (0); }

  let max = myArray[2];
  let secondMax = myArray[3];

  for (let i = 2; i < myArray.length; i++) {
    if (myArray[i] > max) {
      secondMax = max;
      max = myArray[i];
    } else if (myArray[i] > secondMax && myArray[i] < max) {
      secondMax = myArray[i];
    }
  }
  return (secondMax);
}

console.log(second(process.argv));
