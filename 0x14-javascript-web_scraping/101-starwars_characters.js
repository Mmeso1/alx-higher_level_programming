#!/usr/bin/node

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    return;
  }
  const data = JSON.parse(body);
  data.characters.forEach((character)=>{
	  request(character, (error, response, body) => {
		  if (error) {
			  return;
		  }
		  const actor = JSON.parse(body);
		  console.log(actor.name);
	  });
  });
});
