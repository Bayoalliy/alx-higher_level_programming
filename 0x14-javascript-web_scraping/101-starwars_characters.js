#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${id}`;

function requestAsync (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (err, res, body) => {
      if (err) {
        return reject(err);
      }
      resolve(body);
    });
  });
}

async function fetchData () {
  const body = await requestAsync(endpoint);
  for (const character of body.characters) {
    try {
      const charName = await requestAsync(character);
      console.log(charName.name);
    } catch (err) {
      console.log(err);
    }
  }
}

fetchData().catch(err => {
  console.error(err);
});
