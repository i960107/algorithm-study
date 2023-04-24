function solution(want, number, discount) {
  answer = 0;

  const isMatch = (discount) => {
    hash = {};
    for (let d of discount) {
      hash[d] = (hash[d] || 0) + 1;
    }
    let enough = true;
    want.forEach((w, i) => {
      if (hash[w] !== number[i]) enough = false;
    });
    return enough;
  };

  for (let i = 0; i <= discount.length - 10; i++) {
    if (isMatch(discount.slice(i, i + 10))) answer += 1;
  }

  return answer;
}

// 실패
function solution(want, number, discount) {
  answer = 0;
  hash = {};
  for (let i = 0; i < 10; i++) {
    hash[discount[i]] = (hash[discount[i]] || 0) + 1;
  }

  if (want.filter((w, i) => hash[w] === number[i]).length === want.length)
    answer++;

  for (let i = 0; i < discount.length; i++) {
    hash[discount[i]] -= 1;
    hash[discount[i + 10]] = (hash[discount[i + 10]] || 0) + 1;

    if (want.filter((v, i) => hash[v] === number[i]).length === want.length)
      answer++;
  }

  return answer;
}
