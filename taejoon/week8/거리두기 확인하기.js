function solution(places) {
  var answer = [];
  for (let place of places) {
    answer.push(geridogi(place));
  }
  return answer;
}

function geridogi(place) {
  const people = [];
  // 사람 찾기
  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      if (place[i][j] === 'P') people.push([i, j]);
    }
  }

  // 사람이 한명 이하면 거리두기 실패 사람이 13명 초과면 거리두기 불가능
  if (people.length < 2) return 1;
  if (people.length > 13) return 0;

  for (let i = 0; i < people.length; i++) {
    for (let j = i + 1; j < people.length; j++) {
      const [r1, c1] = people[i];
      const [r2, c2] = people[j];
      const distance = Math.abs(r1 - r2) + Math.abs(c1 - c2);
      if (distance === 1) return 0;
      if (distance > 2) continue;

      // 맨해튼 거리가 2인 경우
      if (r1 === r2) {
        if (place[r1][Math.min(c1, c2) + 1] === 'O') return 0;
        else continue;
      }
      if (c1 === c2) {
        if (place[Math.min(r1, r2) + 1][c1] === 'O') return 0;
        else continue;
      }
      if (r1 !== r2 && c1 !== c2) {
        if (place[r1][c2] === 'O' || place[r2][c1] === 'O') {
          return 0;
        }
      }
    }
  }
  return 1;
}
