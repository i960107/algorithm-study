function solution(fees, records) {
  let hash = {};
  const answer = [];

  for (const recode of records) {
    const [time, car] = recode.split(' ');
    hash[car] = hash[car] ? [...hash[car], time] : [time];
  }
  let keys = Object.keys(hash);
  keys.sort();

  for (const key of keys) {
    const recode = hash[key];
    if (recode.length % 2 === 1) recode.push('23:59');
    let timeOfDay = 0;

    while (recode.length > 0) {
      const outTime = recode.pop();
      const inTime = recode.pop();
      timeOfDay += calculateTime(inTime, outTime);
    }

    let sum = 0;

    if (timeOfDay <= fees[0]) sum += fees[1];
    else {
      sum += fees[1] + Math.ceil((timeOfDay - fees[0]) / fees[2]) * fees[3];
    }
    answer.push(sum);
  }
  return answer;
}

function calculateTime(inTime, outTime) {
  let [hour1, minute1] = inTime.split(':').map(Number);
  let [hour2, minute2] = outTime.split(':').map(Number);

  if (minute1 > minute2) {
    hour2 -= 1;
    minute2 += 60;
  }

  return (hour2 - hour1) * 60 + minute2 - minute1;
}
