#!/usr/bin/node


const axios = require('axios');
const movieId = process.argv[2];

export default function getMovieCharacters(movieId) {
    const url = `https://intranet.alxswe.com/rltoken/gh_NaSUk9QlXHVoACFU-tg`
    return axios.get(url)
        .then(response => {
            const characters = response.data.characters;
            return characters;
        })
        .catch(error => {
            console.error('Error fetching movie characters:', error.message):
            return [];
        });
}
async function main() {
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
                console.error('Error fetching character details:', errow.message);
            }
        }
    } else {
        console.log('No characters found for provided Movie ID');
    }
}

main()