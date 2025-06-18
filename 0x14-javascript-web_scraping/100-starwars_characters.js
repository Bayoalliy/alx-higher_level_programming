#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(endpoint, { json: true }, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  for (const character of body.characters) {
    request(character, { json: true }, (err, res, body) => {
      console.log(body.name);
    });
  }
});
