#!/usr/bin/node
module.exports =  class Square extends require('./4-rectangle') {
    /* This is a Square class implentation of inheritance*/
    constructor(size) {
        super(size, size);
      }
};