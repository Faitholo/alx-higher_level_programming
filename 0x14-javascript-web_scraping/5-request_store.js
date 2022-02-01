#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
