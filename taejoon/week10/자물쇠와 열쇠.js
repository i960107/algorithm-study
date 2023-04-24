function solution(key, lock) {
  const hoom = [
    [Infinity, Infinity],
    [-1, -1],
  ];

  // key의 가장자리를 찾습니다.
  for (let i = 0; i < lock.length; i++) {
    for (let j = 0; j < lock[0].length; j++) {
      if (lock[i][j] === 0) {
        if (i < hoom[0][0]) hoom[0][0] = i;
        if (i > hoom[1][0]) hoom[1][0] = i;
        if (j < hoom[0][1]) hoom[0][1] = j;
        if (j > hoom[1][1]) hoom[1][1] = j;
      }
    }
  }

  // 홈 부분만 스캔
  const target = [];
  for (let i = hoom[0][0]; i <= hoom[1][0]; i++) {
    let t = [];
    for (let j = hoom[0][1]; j <= hoom[1][1]; j++) {
      t.push(lock[i][j] === 1 ? 0 : 1);
    }
    target.push(t);
  }

  // 홈을 4방향으로 회전시켜서 가능한 key로 저장
  const keys = locateKeys(target);

  // key에 가능한 k가 있는지 확인
  for (const k of keys) {
    if (check(key, k)) return true;
  }
  return false;
}

function locateKeys(key) {
  const keys = [];
  for (let i = 0; i < 4; i++) {
    keys.push(key);
    key = rotate(key);
  }
  return keys;
}

function rotate(key) {
  const newKey = [];
  for (let i = 0; i < key.length; i++) {
    let t = [];
    for (let j = key.length - 1; j >= 0; j--) {
      t.push(key[j][i]);
    }
    newKey.push(t);
  }
  return newKey;
}

function check(key, target) {
  for (let i = 0; i < key.length - target.length + 1; i++) {
    for (let j = 0; j < key.length - target.length + 1; j++) {
      if (checkTarget(key, target, i, j)) return true;
    }
  }
  return false;
}

function checkTarget(key, target, x, y) {
  for (let i = 0; i < target.length; i++) {
    for (let j = 0; j < target.length; j++) {
      if (key[x + i][y + j] === 0 && target[i][j] === 1) return false;
    }
  }
  return true;
}

// 23, 25, 33, 37 cases failed
