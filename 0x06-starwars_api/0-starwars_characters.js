#!/usr/bin/node

const axios = require('axios');
const movieId = process.argv[2];

function getMovieCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  return axios.get(url)
    .then(response => {
      const characters = response.data.characters;
      return characters;
    })
    .catch(error => {
      console.error('Error fetching movie characters:', error.message);
      return [];
    });
}
async function main () {
  if (!movieId) {
    console.log('Provide the movie ID');
    return;
  }
  const characters = await getMovieCharacters(movieId);
  if (characters.length > 0) {
    for (const characterUrl of characters) {
      try {
        const characterResponse = await axios.get(characterUrl);
        console.log(characterResponse.data.name);
      } catch (error) {
        console.error('Error fetching character details:', error.message);
      }
    }
  } else {
    console.log('No characters found for provided Movie ID');
  }
}

main();
