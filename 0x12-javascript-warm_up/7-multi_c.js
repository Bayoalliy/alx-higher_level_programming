#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (Number(args[2])) {
  let i = parseInt(args[2]);

  while (i > 0) {
    console.log('C is fun');
    i--;
  }
} else {
  console.log('Missing number of occurrences');
}
