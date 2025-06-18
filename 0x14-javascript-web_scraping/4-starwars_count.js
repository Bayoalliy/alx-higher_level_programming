#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, res, body) => {
  let count = 0;
  if (err) {
    console.log(err);
    return;
  }
  for (const film of JSON.parse(body).results) {
    for (const actorsUrl of film.characters) {
      if (actorsUrl.search('18') > 0) {
        count += 1;
      }
    }
  }
  console.log(count);
});
