function solution(board) {
  const N = board.length;
  const visited = new Set()
  const q = [[0, 0, 0, 1, 0]];
  visited[0][0] = 1;

  while (q.length) {
    console.log(q);
    const [x1, y1, x2, y2, time] = q.shift();

    if ((x1 === N - 1 && y1 === N - 1) || (x2 === N - 1 && y2 === N - 1)) {
      return time;
    }

    // 상하좌우 이동
    const dx = [0, 0, -1, 1];
    const dy = [-1, 1, 0, 0];

    for (let i = 0; i < 4; i++) {
      const nx1 = x1 + dx[i];
      const ny1 = y1 + dy[i];
      const nx2 = x2 + dx[i];
      const ny2 = y2 + dy[i];

      if (
        nx1 < 0 ||
        ny1 < 0 ||
        nx2 < 0 ||
        ny2 < 0 ||
        nx1 >= N ||
        ny1 >= N ||
        nx2 >= N ||
        ny2 >= N ||
        board[nx1][ny1] === 1 ||
        board[nx2][ny2] === 1 ||
        (visited[nx1][ny1] && visited[nx2][ny2])
      )
        continue;

      visited[nx1][ny1] = 1;
      visited[nx2][ny2] = 1;
      q.push([nx1, ny1, nx2, ny2, time + 1]);
    }

    // 회전
    if (x1 === x2) {
      // 가로
      // 위로 회전
      if (x1 - 1 >= 0 && board[x1 - 1][y1] === 0 && board[x2 - 1][y2] === 0) {
        if (!(visited[x1 - 1][y1])) {
          visited[x1 - 1][y1] = 1;
          q.push([x1 - 1, y1, x1, y1, time + 1]);
        }
        if (!visited[x2 - 1][y2]) {
          visited[x2 - 1][y2] = 1;
          q.push([x2 - 1, y2, x2, y2, time + 1]);
        }
      }
      // 아래로 회전
      if (x1 + 1 < N && board[x1 + 1][y1] === 0 && board[x2 + 1][y2] === 0) {
        if (!visited[x1 + 1][y1]) {
          visited[x1 + 1][y1] = 1;
          q.push([x1, y1, x1 + 1, y1, time + 1]);
        }
        if (!visited[x2 + 1][y2]) {
          visited[x2 + 1][y2] = 1;
          q.push([x2, y2, x2 + 1, y2, time + 1]);
        }
      }
    } else {
      // 세로
      // 왼쪽으로 회전
      if (y1 - 1 >= 0 && board[x1][y1 - 1] === 0 && board[x2][y2 - 1] === 0) {
        if (!visited[x1][y1 - 1]) {
          visited[x1][y1 - 1] = 1;
          q.push([x1, y1 - 1, x1, y1, time + 1]);
        }
        if (!visited[x2][y2 - 1]) {
          visited[x2][y2 - 1] = 1;
          q.push([x2, y2 - 1, x2, y2, time + 1]);
        }
      }
      // 오른쪽으로 회전
      if (y1 + 1 < N && board[x1][y1 + 1] === 0 && board[x2][y2 + 1] === 0) {
        if (!visited[x1][y1 + 1]) {
          visited[x1][y1 + 1] = 1;
          q.push([x1, y1, x1, y1 + 1, time + 1]);
        }
        if (!visited[x2][y2 + 1]) {
          visited[x2][y2 + 1] = 1;
          q.push([x2, y2, x2, y2 + 1, time + 1]);
        }
      }
    }
  }
}
