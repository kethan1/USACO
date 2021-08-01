const fs = require('fs'),
    { EOL } = require('os');


const cows = fs.readFileSync('outofplace.in', 'utf8').split(EOL).slice(1).map((element) => Number(element))

let swaps = -1;
for ([index, cow] in Object.entries([...cows].sort())) {
    if (cows[index] !== cow) {
        swaps++;
    }
}

fs.writeFileSync('outofplace.out', swaps.toString());
