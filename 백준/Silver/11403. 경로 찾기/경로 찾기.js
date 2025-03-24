let input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = parseInt(input[0]);

let MAP = [];

for (let i = 1; i < N + 1; i++) {
  MAP.push(input[i].trim().split(" ").map(Number));
}

for (let k = 0; k < N; k++) {
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (MAP[i][k] && MAP[k][j]) {
        MAP[i][j] = 1;
      }
    }
  }
}

for (let i = 0; i < N; i++) {
  console.log(MAP[i].join(" "));
}
