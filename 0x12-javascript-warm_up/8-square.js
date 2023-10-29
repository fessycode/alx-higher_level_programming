#!/usr/bin/node

const count = Number(process.argv[2]);
const symbol = 'X';
let square = '';
let a;

if (!count) {
  console.log('Missing size');
}

for (a = 0; a < count; a++) {
  square = square + symbol;
}

for (a = 0; a < count; a++) {
  console.log(square);
}
