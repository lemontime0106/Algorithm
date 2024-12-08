const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
let stars = []

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    const N = Number(input[0])
    
    for (let i=1; i <= N; i++) {
        let star = ""
        for (let j=0; j < i; j++) {
            star += "*"
        }
        stars.push(star)
    }
    
    for (let star of stars) {
        console.log(star)
    }
    
});