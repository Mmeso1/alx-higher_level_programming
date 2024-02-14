#!/usr/bin/node

function findSecondLargest (args) {
  if (args.length <= 1) {
    console.log(0);
  } else {
    const integers = args.map(Number).sort((a, b) => b - a);
    console.log(integers[1]);
  }
}

const args = process.argv.slice(2);
findSecondLargest(args);
