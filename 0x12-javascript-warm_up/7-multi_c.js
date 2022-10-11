#!/usr/bin/node

const lang = 'C is fun';
const times = process.argv;
let i = 0;
if (isNaN(times[2])) {
  console.log('Missing number of occurrences');
}
while (i < times[2]) {
  console.log(lang);
  i++;
}
