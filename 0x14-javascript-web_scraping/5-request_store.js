#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const link = process.argv[2];

const file = process.argv[3];

request(link, function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  writer(body);
});

function writer (page) {
  fs.writeFile(file, page, 'UTF-8', function (error) {
    if (error) {
      console.log(error);
    }
  });
}
