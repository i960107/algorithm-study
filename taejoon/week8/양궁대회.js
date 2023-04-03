function solution(n, info) {
  const lion = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  let maxScore = 0;
  let visited = Array(11).fill(false);
  let boards = new Set();

  // find all possible cases
  function dfs(arrow, score) {
    if (arrow === 0) {
      let peach_score = 0;
      let lion_score = 0;
      let lionBoard = [...visited.map((v, i) => (v ? info[i] + 1 : 0))];
      for (let i = 0; i < info.length; i++) {
        if (lionBoard[i] > info[i] && lionBoard[i] > 0) {
          lion_score += 10 - i;
        }
        if (info[i] > lionBoard[i] && info[i] > 0) {
          peach_score += 10 - i;
        }
      }
      let score = lion_score - peach_score;
      const before = maxScore;
      maxScore = Math.max(maxScore, score);
      if (maxScore > before) boards = new Set();
      if (maxScore === score) boards.add(JSON.stringify([...lionBoard]));
    }

    for (let i = 0; i < 11; i++) {
      if (!visited[i] && arrow >= info[i] + 1) {
        visited[i] = true;
        dfs(arrow - info[i] - 1, score + 10 - i);
        visited[i] = false;
      }
    }
  }
  dfs(n, 0);

  const answers = Array.from(boards);
  answers.sort(sorting);
  console.log(answers);
  return answers.length ? JSON.parse(answers[answers.length - 1]) : [-1];
}

function sorting(boardA, boardB) {
  for (let i = boardA.length - 1; i >= 0; i--) {
    if (boardA[i] > boardB[i]) return 1;
    if (boardA[i] === boardB[i]) continue;
    else {
      return -1;
    }
  }
}
