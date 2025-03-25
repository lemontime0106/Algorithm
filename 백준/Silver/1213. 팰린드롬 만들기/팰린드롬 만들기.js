const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim();

const word = input;
const dict = {};

for (let char of word) {
  dict[char] = dict[char] ? dict[char] + 1 : 1;
}

let oddCount = 0;
let mid = "";
let start = "";

for (let char in dict) {
  if (dict[char] % 2 === 1) {
    oddCount++;
    mid = char;
    if (oddCount > 1) {
      console.log("I'm Sorry Hansoo");
      return;
    }
  }
}

const sortedKeys = Object.keys(dict).sort();

for (let char of sortedKeys) {
  start += char.repeat(Math.floor(dict[char] / 2));
}

const end = start.split("").reverse().join("");
console.log(start + mid + end);
