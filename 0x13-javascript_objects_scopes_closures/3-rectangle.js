#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    let loop = this.height;
    while (loop > 0) {
      console.log('X'.repeat(this.width));
      loop--;
    }
  }
};
