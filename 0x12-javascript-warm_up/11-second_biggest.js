#!/usr/bin/node

const args = process.argv;
const array = args.slice(2).sort();
const ans = array.slice(-2, -1)[0];
if (isNaN(ans)) {
  console.log(0);
} else {
  console.log(ans);
}
