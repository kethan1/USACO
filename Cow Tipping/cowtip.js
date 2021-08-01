const fs = require('fs'),
    { EOL } = require('os');

const cows = fs.readFileSync('cowtip.in', 'utf8').split(EOL).slice(1).map((element) => element.split("").map((element) => Number(element)))

function cow_tipper(pos2_x, pos2_y, cowsList) {
    for (let index=0; index < pos2_x + 1; index++) {
        for (let index2=0; index2 < pos2_y + 1; index2++) {
            cowsList[index][index2] = 1 - cowsList[index][index2]  // flips the cow (converts 1 to 0 and 0 to 1)
        }
    }
}

let cow_tippers_used = 0;
for (let index = cows.length - 1; index > -1; index--) {
    for (let index2 = cows[index].length - 1; index2 > -1; index2--) {
        if (cows[index][index2]) {
            cow_tipper(index, index2, cows)
            cow_tippers_used += 1  
        }
    }
}

fs.writeFileSync('cowtip.out', cow_tippers_used.toString()); 
