#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const tasks = {};

  for (const todo of JSON.parse(body)) {
    if (todo.completed === true) {
      if (todo.userId.toString() in tasks) {
        tasks[todo.userId.toString()] += 1;
      } else {
        tasks[todo.userId.toString()] = 1;
      }
    }
  }
  console.log(tasks);
});
