#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = this.height; i > 0; i--) {
      let str = '';
      for (let j = this.width; j > 0; j--) {
        str += 'X';
      } console.log(str);
    }
  }
}

module.exports = Rectangle;
