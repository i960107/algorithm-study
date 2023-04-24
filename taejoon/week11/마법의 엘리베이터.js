function solution(storey) {
  let answer = 0;
  // 일의자리 p를 구한다.
  // p=1-4이면 아래로 이동
  // p=6-10층이면 위로 이동
  // p=5이면 십의자리가 5이상이면 위로, 5미만이면 아래로 이동
  while (storey > 0) {
    let p = storey % 10;
    if (p > 5) {
      answer += 10 - p;
      storey += 10;
    } else if (p === 5 && (storey + '')[(storey + '').length - 2] >= 5) {
      answer += 10 - p;
      storey += 10;
    } else {
      answer += p;
    }
    storey = Math.floor(storey / 10);
  }
  return answer;
}
