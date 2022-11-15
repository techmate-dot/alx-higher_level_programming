#!/usr/bin/node

let logs = -1;
exports.logMe = function (item) {
  ++logs;
  console.log(logs + ': ' + item);
};
