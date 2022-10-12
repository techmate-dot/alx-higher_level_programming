#!/usr/bin/node

const arg = process.argv;

function add (a, b) {
  return Number(a) + Number(b);
}
const added = add(arg[2], arg[3]);
console.log(added);
