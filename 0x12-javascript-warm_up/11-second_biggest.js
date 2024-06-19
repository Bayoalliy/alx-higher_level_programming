#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (args.length === 3) {
  console.log(parseInt(args[2]));
} else if (args.length > 3) {
  const newArgs = [];
  for (let i = 2; i < args.length; i++) {
    newArgs.push(parseInt(args[i]));
  }
  newArgs.sort();
  console.log(newArgs[newArgs.length - 2]);
} else {
  console.log(0);
}
