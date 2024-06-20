#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    for (let i = this.height; i > 0; i--) {
      let str = '';
      for (let j = this.width; j > 0; j--) {
        if (c) {
          str += c;
        } else {
          str += 'X';
        }
      } console.log(str);
    }
  }
}

module.exports = Square;
