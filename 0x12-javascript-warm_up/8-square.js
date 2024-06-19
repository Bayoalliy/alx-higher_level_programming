#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (Number(args[2])) {
  const size = parseInt(args[2]);

  for (let i = size; i > 0; i--) {
    let str = '';
    for (let j = size; j > 0; j--) {
      str += 'X';
    } console.log(str);
  }
} else {
  console.log('Missing size');
}
