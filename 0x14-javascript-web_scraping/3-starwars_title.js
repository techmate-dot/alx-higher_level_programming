#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const link = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(link, function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  const movie = JSON.parse(body);
  console.log(movie.title);
  console.log(link);
}
);
