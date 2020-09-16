#!/usr/bin/node
// prints x times “C is fun”

if (process.argv[2]) {
  let i = 0;
  while (i < process.argv[2]) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
