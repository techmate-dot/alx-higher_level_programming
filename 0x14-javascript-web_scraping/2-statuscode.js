#!/usr/bin/node

const request = require('request');
const link = process.argv[2].toString()

request(link, function (error, response, body) {
if (error) {
  console.error('error:', error);
}
console.log('code:',response.statusCode);
}
);
