#!/usr/bin/node

const Square1 = require('./5-square.js');

module.exports = class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let loop = this.height;
    while (loop > 0) {
      console.log(c.repeat(this.width));
      loop--;
    }
  }
};
