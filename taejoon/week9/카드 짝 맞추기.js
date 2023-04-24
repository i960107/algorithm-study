function solution(board, r, c) {
  const card = new Set();
  const cardMap = new Map();

  for (let i = 0; i < 4; i++) {
    for (let j = 0; j < 4; j++) {
      if (board[i][j] !== 0) {
        card.add(board[i][j]);
        if (cardMap.has(board[i][j])) {
          cardMap.get(board[i][j]).push([i, j]);
        } else {
          cardMap.set(board[i][j], [[i, j]]);
        }
      }
    }
  }

  const cardArr = Array.from(card);
  const cardPermutation = permutaion(cardArr, cardArr.length);

  const bfs = (board, r, c, card) => {
    const visited = new Set();
    const queue = [[r, c, 0]];
    const dr = [-1, 0, 1, 0];
    const dc = [0, 1, 0, -1];
    visited.add(`${r},${c}`);
    while (queue.length) {
      const [r, c, count] = queue.shift();
      if (board[r][c] === card) {
        return count;
      }
      for (let i = 0; i < 4; i++) {
        let nr = r + dr[i];
        let nc = c + dc[i];

        if (nr < 0 || nr >= 4 || nc < 0 || nc >= 4 || board[nr][nc] !== 0) {
          continue;
        }
        
        if (!visited.has(`${nr},${nc}`)) {
          visited.add(`${nr},${nc}`);
          queue.push([nr, nc, count + 1]);
        }
      }
      // ctrl + 방향키
      for (let i = 0; i < 4; i++) {
        let nr = r;
        let nc = c;
        while (true) {
          nr += dr[i];
          nc += dc[i];
          if (nr < 0 || nr >= 4 || nc < 0 || nc >= 4 || board[nr][nc] !== 0) {
            break;
          }
        }
        if (!visited.has(`${nr},${nc}`)) {
          visited.add(`${nr},${nc}`);
          queue.push([nr, nc, count + 1]);
        }
      }
    }
  };

  let answer = Infinity;
  cardPermutation.forEach((card) => {
    let count = 0;
    let boardCopy = board.map((v) => v.slice());
    let rCopy = r;
    let cCopy = c;
    for (let i = 0; i < card.length; i++) {
      const [r1, c1] = cardMap.get(card[i])[0];
      const [r2, c2] = cardMap.get(card[i])[1];
      count += bfs(boardCopy, rCopy, cCopy, card[i]);
      boardCopy[r1][c1] = 0;
      boardCopy[r2][c2] = 0;
      count += bfs(boardCopy, r1, c1, card[i]);
      rCopy = r1;
      cCopy = c1;
    }
    answer = Math.min(answer, count);
  });

  return answer;
}

function permutaion(arr, selectNum) {
  const result = [];
  if (selectNum === 1) return arr.map((v) => [v]);
  arr.forEach((v, idx, arr) => {
    const fixer = v;
    const restArr = arr.filter((_, index) => index !== idx);
    const permuationArr = permutaion(restArr, selectNum - 1);
    const combineFixer = permuationArr.map((v) => [fixer, ...v]);
    result.push(...combineFixer);
  });
  return result;
}
