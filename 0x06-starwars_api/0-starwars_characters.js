#!/usr/bin/node

// Importing the request library
import request from 'request';

// Function to make a request to each URL in an array
const req = (arr, i) => {
  // If we've reached the end of the array, stop recursion
  if (i === arr.length) return;

  // Make a request to the URL at the current index
  request(arr[i], (err, response, body) => {
    // If there's an error, throw it
    if (err) {
      throw err;
    } else {
      // Otherwise, log the name property of the parsed JSON response
      console.log(JSON.parse(body).name);
      // Recursively call the function with the next index
      req(arr, i + 1);
    }
  });
};

// Make a request to the Star Wars API for a specific film
request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (err, response, body) => {
    // If there's an error, throw it
    if (err) {
      throw err;
    } else {
      // Otherwise, get the characters array from the parsed JSON response
      const chars = JSON.parse(body).characters;
      // Call the req function with the characters array and starting index 0
      req(chars, 0);
    }
  }
);
