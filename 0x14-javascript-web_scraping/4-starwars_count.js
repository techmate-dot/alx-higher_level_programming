#!/usr/bin/node

const link = process.argv[2];
const request = require('request');
const ID = '18';

request(link, function (error, response, body) {
  let count = 0;
  if (error) {
    return console.error(error);
  }
  const newBody = JSON.parse(body);
  const result = newBody.results;
  result.forEach(function (element) {
    for (character in element.characters) {
      if (character.includes(ID)) {
        ++count;
      }
    }
  });
  console.log(count - 1);
}
);
