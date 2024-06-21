#!/usr/bin/node

const dict = require('./101-data').dict;

const val = [];
const objVal = Object.values(dict);
for (const i of objVal) {
  let uniq = true;
  for (const j of val) {
    if (i === j) {
      uniq = false;
      break;
    }
  } if (uniq) {
    val.push(i);
  }
}

const newDict = {};

for (const i of val) {
  newDict[i] = [];
  for (const j of Object.keys(dict)) {
    if (dict[j] === i) {
      newDict[i].push(j);
    }
  }
} console.log(newDict);
