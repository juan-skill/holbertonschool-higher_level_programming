#!/usr/bin/node

const request = require('request');
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  method: 'GET'
};

request(options, function (err, response, body) {
  if (err) {
    return console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach(function (element) {
      request(element, function (err, response, body) {
        if (err) {
          return console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
