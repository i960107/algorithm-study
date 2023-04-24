function solution(name) {
  const distance = {
    A: 0,
    B: 1,
    C: 2,
    D: 3,
    E: 4,
    F: 5,
    G: 6,
    H: 7,
    I: 8,
    J: 9,
    K: 10,
    L: 11,
    M: 12,
    N: 13,
    O: 12,
    P: 11,
    Q: 10,
    R: 9,
    S: 8,
    T: 7,
    U: 6,
    V: 5,
    W: 4,
    X: 3,
    Y: 2,
    Z: 1,
  };

  let upDown = 0;
  let leftRight = name.length - 1;

  // i 지점까지 오른쪽으로 이동후 다음 타겟까지 왼쪽으로 이동하는 값을 계속 갱신
  for (let i = 0; i < name.length; i++) {
    upDown += distance[name[i]];
    let nextIndex = i + 1;
    while (nextIndex < name.length && name[nextIndex] === 'A') {
      nextIndex++;
    }

    // 앞에서 뒤로 가는 경우와 뒤에서 앞으로 가는 경우 중 최소값을 구함
    leftRight = Math.min(
      leftRight,
      i + name.length - nextIndex + Math.min(i, name.length - nextIndex)
    );
  }

  return upDown + leftRight;
}

solution('JBABBAKZA'); // Z까지 오른쪽으로 이동후 다음 타겟 없으므로 최소임.
