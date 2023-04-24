function solution(s) {
  let count = Infinity;
  let answers = [];
  for (let i = 1; i < Math.floor(s.length / 2) + 1; i++) {
    let str = '';
    let cnt = 1;
    let f = s.slice(0, i);
    for (let j = i; j < s.length; j += i) {
      if (f === s.slice(j, j + i)) cnt++;
      else {
        if (cnt > 1) str += cnt + f;
        else str += f;
        cnt = 1;
        f = s.slice(j, j + i);
      }
    }
    if (cnt > 1) str += cnt + f;
    else str += f;
    answers.push(str);
  }
  answers.sort((a, b) => a.length - b.length);
  return answers.length > 0 ? answers[0].length : 1;
}
