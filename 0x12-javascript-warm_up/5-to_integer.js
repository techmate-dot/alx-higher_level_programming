#!/usr/bin/node

const args = process.argv;
const validation = Number(args[2]);

if (isNaN(validation)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + validation);
}
