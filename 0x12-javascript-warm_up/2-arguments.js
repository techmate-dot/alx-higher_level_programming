#!/usr/bin/node

const args = process.argv;
const realNum = args.length - 2;

if (realNum === 0) {
  console.log('No argument');
} else if (realNum === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
