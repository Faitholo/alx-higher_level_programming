#!/usr/bin/node
// A script that prints all characters of a Star Wars movie
// Display characters name in the same order of the list  “characters” in the /films/ response

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function printCharacters (characters, idx) {
  request(characters[idx], (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).name);
      if (idx + 1 < characters.length) {
        printCharacters(characters, idx + 1);
      }
    }
  });
}

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});
