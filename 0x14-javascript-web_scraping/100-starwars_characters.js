#!/usr/bin/node
// A script that prints all characters of a Star Wars movie.

#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(url, function (_err, _res, body) {
 const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; ++i) {
    request(characters[i], function (_cErr, _cRes, cBody) {
      console.log(JSON.parse(cBody).name);
    });
  }
});