#!/usr/bin/node

const fs = require('fs');

const path = process.argv[2].toString();
console.log(path);
fs.readFile(path, function (err, data) {
  if (err) {
    return console.error(err);
  }
  console.log(data.toString());
});
