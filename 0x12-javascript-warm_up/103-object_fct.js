#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12,
  incr
};
console.log(myObject);
/*
YOUR CODE HERE
*/

function incr () {
  myObject.value++;
}

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
