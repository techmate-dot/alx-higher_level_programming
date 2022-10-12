#!/usr/bin/node

const num = process.argv;

function factorial(n) {
    if (n === 1) {
      return 1
    }
  return factorial(n - 1) * n
}

const sol = factorial(num[2]);
console.log(sol)