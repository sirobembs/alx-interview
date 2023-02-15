#!/usr/bin/node

//Starwars API


const https = require('https');
const process = require('process');

const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}/`;

https.get(url, (res) => {
  let rawData = '';
  res.on('data', (chunk) => { rawData += chunk; });
  res.on('end', () => {
    try {
      const movie = JSON.parse(rawData);
      const characterUrls = movie.characters;
      characterUrls.forEach((url) => {
        https.get(url, (res) => {
          let rawData = '';
          res.on('data', (chunk) => { rawData += chunk; });
          res.on('end', () => {
            try {
              const character = JSON.parse(rawData);
              console.log(character.name);
            } catch (error) {
              console.error(error.message);
            }
          });
        }).on('error', (error) => {
          console.error(error.message);
        });
      });
    } catch (error) {
      console.error(error.message);
    }
  });
}).on('error', (error) => {
  console.error(error.message);
});

