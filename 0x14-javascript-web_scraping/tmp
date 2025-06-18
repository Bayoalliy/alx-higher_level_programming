#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, res, body) => {
  let count = 0;
  const wedge = 'https://swapi-api.alx-tools.com/api/people/18/';
  if (err) {
    console.log(err);
    return;
  }
  for (const film of JSON.parse(body).results) {
    for (const actorsUrl of film.characters) {
      if (actorsUrl === wedge) {
        count += 1;
      }
    }
  }
  console.log(count);
});
