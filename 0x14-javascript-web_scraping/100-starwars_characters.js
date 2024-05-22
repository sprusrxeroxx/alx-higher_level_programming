#!/usr/bin/node
// A script that prints all characters of a Star Wars movie.

const request = require('request');
const url = process.argv[2];

request(url, function (error, _response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, function (error, _response, body) {
        if (error) {
          console.error('error:', error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});