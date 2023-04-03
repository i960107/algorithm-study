function solution(id_list, report, k) {
  let hash = {};
  let answer = Array(id_list.length).fill(0);
  for (let i = 0; i < report.length; i++) {
    const [userA, userB] = report[i].split(' ');
    if (hash[userB]) hash[userB].add(userA);
    else {
      hash[userB] = new Set();
      hash[userB].add(userA);
    }
  }
  for (const [key, value] of Object.entries(hash)) {
    if (value.size >= k) {
      for (const user of value) {
        answer[id_list.indexOf(user)]++;
      }
    }
  }
  return answer;
}
