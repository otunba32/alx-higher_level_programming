#!/usr/bin/node
const a = process.argv[2];
if (parseInt(a)) {
  for (let p = 0; p < a; p++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
