#!/usr/bin/node

const _dict = require('./101-data.js').dict;

const newDict = {};

for (const key in _dict) {
  const occurrence = _dict[key];

  if (Object.prototype.hasOwnProperty.call(occurrence)) {
    newDict[occurrence].push(key);
  } else {
    newDict[occurrence] = [key];
  }
}

console.log(newDict);
