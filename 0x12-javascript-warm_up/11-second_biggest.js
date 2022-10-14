#!/usr/bin/node

const args = process.argv;
const array = args.slice(2);
const max = Number(Math.max(...array));
let smax = 0;
array.forEach((element) => {
  if (Number(element) < max && Number(element) > smax) {
    smax = element;
  }
});
console.log(smax);
