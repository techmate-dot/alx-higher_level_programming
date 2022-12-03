#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2].toString();
const sentence = process.argv[3].toString();

fs.writeFile(file, sentence, 'utf-8', function (error) {
  if (error) {
    console.error(error);
  }
}
);
