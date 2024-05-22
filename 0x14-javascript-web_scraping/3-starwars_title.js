#!/usr/bin/node
// A script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log(JSON.parse(response.body).title);
  }
});