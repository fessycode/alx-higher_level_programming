#!/usr/bin/node

let x;

for (x = 0; process.argv[x]; x++) {
  continue;
}

console.log(x === 2 ? 'No argument' : process.argv[2]);
