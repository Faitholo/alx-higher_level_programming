#!/usr/bin/node
// Script class Rectangle that defines a rectangle

const Rectangle = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let prints = '';
    for (let cont1 = 0; cont1 < this.height; cont1++) {
      for (let cont = 0; cont < this.width; cont++) {
        prints = prints + 'X';
      }
      console.log(prints);
      prints = '';
    }
  }
};

module.exports = Rectangle;
