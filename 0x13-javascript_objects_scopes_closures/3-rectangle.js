#!/usr/bin/node
module.exports = class Rectangle {
    
    constructor (w, h) {
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
          }
    }
    print(width, height){
        for (let i = 0; i < height; i++)
        {
            console.log("x")*width;
        }
    }
  };