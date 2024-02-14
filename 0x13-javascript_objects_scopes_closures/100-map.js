#!/usr/bin/node

const list = require('./100-data.js');

console.log(list.list);

const newList = list.list.map((index, val) => {
  return index * val
});
console.log(newList);
