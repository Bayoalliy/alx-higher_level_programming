#!/usr/bin/node

const fs = require('fs');
const process = require('process');
const args = process.argv;

const txt1 = fs.readFileSync(args[2], 'utf-8');
const txt2 = fs.readFileSync(args[3], 'utf-8');
const txt3 = txt1 + txt2;
fs.writeFileSync(args[4], txt3);
