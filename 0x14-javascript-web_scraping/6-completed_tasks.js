#!/usr/bin/node

const request = require('request');

const link = process.argv[2];

request(link, 'get', function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  const newBody = JSON.parse(body);
  const taskCount = {};
  newBody.forEach(function (element) {
    if (element.completed) {
      const userId = element.userId;
      if (userId in taskCount) {
        taskCount[userId] += 1;
      } else {
        taskCount[userId] = 1;
      }
    }
  });
  console.log(taskCount);
});
