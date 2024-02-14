#!/usr/bin/node
// defines a square and inherits from Square of 5-square.js

const OldSquare = require('./5-square');

module.exports = class Square extends OldSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint(c = 'X') {
    super.print(c);
  }
};
