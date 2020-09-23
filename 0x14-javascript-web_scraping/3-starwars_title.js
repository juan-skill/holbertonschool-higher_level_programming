#!/usr/bin/node

const request = require('request');

const reqURL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(reqURL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
