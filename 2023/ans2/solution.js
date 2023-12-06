const fs = require('fs');


const part1 = () => {
  const input = fs.readFileSync('input.txt', 'utf-8');

  limits = {
    red: 12,
    green: 13,
    blue: 14
  };

  const lines = input.split('\n');
  let sum = 0
  for(let line of lines) {
    const [game_id, games] = line.split(':');
    const id = parseInt(game_id.split(' ')[1]);
    let possible = true;

    for (let game of games.split(';')) {
      const rolls = game.split(',')
      for (let roll of rolls) {
        const [number, color] = roll.trim().split(' ');
        if (limits[color] < parseInt(number)) {
          possible = false;
        }
      }
      
    }

    if (possible) {
      sum += id;
    }
  }

  return sum;
}

const part2 = () => {
  const input = fs.readFileSync('input.txt', 'utf-8');

  const lines = input.split('\n');

  let ans = 0;

  let maxes = {
    red: 2**32,
    blue: 2**32,
    green: 2**32
  }
  for (let line of lines) {
    const [game_id, games] = line.split(':');

    for (let game of games.split(';')) {
      const rolls = game.split(',')
      for (let roll of rolls) {
        const [number, color] = roll.trim().split(' ');
        maxes[color] = Math.min(maxes[color], parseInt(number));
      }
    }

    ans += maxes.red == 2**32 ? 1 : maxes.red * maxes.blue == 2**32 ? 1 : maxes.blue * maxes.green == 2**32 ? 1: maxes.green;
  }
  return ans
}

console.log(part1(), part2());