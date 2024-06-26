#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');
const url = process.argv[2];

request(url, function (error, _response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', function (error) {
      if (error) {
        console.error('error:', error);
      }
    });
  }
});