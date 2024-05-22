#!/usr/bin/node
// A Script that reads and prints the content of a file.

const fs = require('fs');

fs.readFile(process.argvp[2], 'utf8', function(err, data) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});