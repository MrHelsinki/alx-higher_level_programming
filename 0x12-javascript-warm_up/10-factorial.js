#!/usr/bin/node

const { argv } = require('process');

if (!isNaN) {
  const num = parseInt(argv[2]);
  console.log(factorial(num));
} else {
  console.log(1);
}

function factorial (num) {
  if (num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
