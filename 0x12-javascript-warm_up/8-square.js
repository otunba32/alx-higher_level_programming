#!/usr/bin/node
const a = process.argv[2];
let x = 0;
let square = '';
if (parseInt(a)) {
  for (let p = 0; p < a; p++) {
    while (x < a) {
      square += 'M';
      x++;
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
