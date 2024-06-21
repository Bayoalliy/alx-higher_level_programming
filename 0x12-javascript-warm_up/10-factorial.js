#!/usr/bin/node

const process = require('process');
const args = process.argv;

function factorial (num) {
  if (num === 0) {
    return (1);
  } return (num * factorial(num - 1));
}

if (Number(args[2])) {
  console.log(factorial(parseInt(args[2])));
} else {
  console.log(1);
}
