#!/usr/bin/node

const times = process.argv;
const block = 'X';

if (isNaN(times[2])) {
  console.log('Missing size');
}
for (let i = 0; i < times[2]; i++) {
  console.log(block.repeat(times[2]));
}
