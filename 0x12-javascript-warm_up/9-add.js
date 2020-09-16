#!/usr/bin/node
// prints the addition of 2 integers

const numberOne = parseInt(process.argv[2]);
const numbertwo = parseInt(process.argv[3]);

if (isNaN(numberOne) || isNaN(numbertwo)) {
  console.log('NaN');
} else {
  console.log(add(numberOne, numbertwo));
}

function add (a, b) {
  return a + b;
}
