#!/usr/bin/node
const arg = process.argv[3];
if (arg) {
  console.log(arg);
} else {
  console.log('No argument');
}
