#!/usr/bin/env node
let result = 0;
import { open } from 'fs/promises';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));

const numberMap = {
  zero: 0,
  one: 1,
  two: 2,
  three: 3,
  four: 4,
  five: 5,
  six: 6,
  seven: 7,
  eight: 8,
  nine: 9,
};

const appendNumbers = (line) => {
  let updatedLine = line;
  for (const word in numberMap) {
    const regex = new RegExp(`(?=${word})`, 'g');
    updatedLine = updatedLine.replace(regex, (match, offset) => {
      if (updatedLine.substr(offset, word.length) === word) {
        return word + numberMap[word];
      }
      return match;
    });
  }
  return updatedLine;
};

const readFile = async (path) => {
  const filePath = join(__dirname, path);
  const file = await open(filePath, 'r');
  for await (const line of file.readLines()) {
    const updatedLine = appendNumbers(line);
    console.log(updatedLine);
    const match = updatedLine.match(/(\d{1}).*(\d{1})/);
    
    if (match) {
      let combinedNumber = match[1] + match[2];
      result += parseInt(combinedNumber);
    } else {
      const match = updatedLine.match(/(\d)/);
      if (match) {
        let combinedNumber = match[1] + match[1];
        result += parseInt(combinedNumber);
      }
    }
  }
};


await readFile('./input');

console.log(result);