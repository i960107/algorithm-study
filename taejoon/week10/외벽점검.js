function solution(n, weak, dist) {
  const weakLen = weak.length;
  const distLen = dist.length;
  const weakList = weak.map((v, i) => {
    const weakList = [];
    for (let j = 0; j < weakLen; j++) {
      weakList.push(weak[(i + j) % weakLen]);
    }
    return weakList;
  });
  const distList = dist.map((v, i) => {
    const distList = [];
    for (let j = 0; j < distLen; j++) {
      distList.push(dist[(i + j) % distLen]);
    }
    return distList;
  });
  const result = [];
  for (let i = 0; i < weakLen; i++) {
    for (let j = 0; j < distLen; j++) {
      const weak = weakList[i];
      const dist = distList[j];
      let count = 1;
      let start = weak[0];
      for (let k = 0; k < weakLen; k++) {
        if (start + dist[count - 1] < weak[k]) {
          count++;
          start = weak[k];
        }
      }
      result.push(count);
    }
  }
  return Math.min(...result);
}
