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
  newArgs.sort((a, b) => b - a);
  if (newArgs[0] !== newArgs[1]) {
    console.log(newArgs[1]);
  } else if (newArgs[0] === newArgs[newArgs.length - 1]) {
    console.log(newArgs[0]);
  } else {
    for (const j of newArgs) {
      if (j < newArgs[0]) {
        console.log(j);
        break;
      }
    }
  }
} else {
  console.log(0);
}
