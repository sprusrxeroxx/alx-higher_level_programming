#!/usr/bin/node
// A Script that reads and prints the content of a file.

import { readFile } from 'fs';
const file = process.argv[2];

readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});