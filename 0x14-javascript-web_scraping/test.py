#!/usr/bin/node

const request = require('request');

const link = process.argv[2];

request(link, 'get', function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  const newBody = JSON.parse(body);
  let num = newBody[0].userId;
  let taskCompleted = 0;
  const dict = {};
  newBody.forEach(function (element) {
    // console.log(element.userId);
    const userid = element.userId;
    if (userid !== num) {
      dict[num] = taskCompleted;
      num = userid;
      taskCompleted = 0;
    }
    if (userid === num) {
      if (element.completed === true) {
        ++taskCompleted;
      }
    }
  });
  dict[num] = taskCompleted;
  console.log(dict);
});
