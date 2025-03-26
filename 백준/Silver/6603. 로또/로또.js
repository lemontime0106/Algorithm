const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

let answer = [];

for (let i = 0; i < input.length; i++) {
  const lst = input[i].split(" ").map(Number);
  const N = lst.shift();

  if (N === 0) break;

  const visited = new Array(N).fill(false);
  const result = [];
  let temp = [];

  function dfs(start) {
    if (result.length === 6) {
      temp.push([...result]);
      return;
    }

    for (let j = start; j < N; j++) {
      if (!visited[j]) {
        visited[j] = true;
        result.push(lst[j]);
        dfs(j + 1);
        result.pop();
        visited[j] = false;
      }
    }
  }

  dfs(0);
  answer.push(temp);
}

console.log(
  answer
    .map((group) => group.map((comb) => comb.join(" ")).join("\n"))
    .join("\n\n")
);
