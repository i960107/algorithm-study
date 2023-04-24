function solution(plans) {
  const answer = [];
  plans.sort((a, b) => convertToMinute(b[1]) - convertToMinute(a[1]));
  const stack = [];
  while (plans.length || stack.length) {
    const [name, start, playTime] = plans.pop();
    const endTime = convertToMinute(start) + parseInt(playTime);

    // 마지막 과제를 시작한 경우 과제 종료후 이전에 수행중이던 과제들을 순차적으로 수행합니다.
    if (plans.length === 0) {
      answer.push(name);
      while (stack.length) {
        answer.push(stack.pop()[0]);
      }
      break;
    }

    const nextStart = convertToMinute(plans[plans.length - 1][1]);
    const leftTime = endTime - nextStart;

    // 수행중인 과제가 끝나지 않으면 스택에 담습니다.
    if (leftTime > 0) {
      stack.push([name, leftTime]);
    } else if (leftTime === 0) {
      answer.push(name);
    } else {
      // 과제가 끝나고 시간이 남는지를 확인합니다.
      answer.push(name);
      let currentTime = endTime;
      while (stack.length) {
        const [stackName, stackLeftTime] = stack.pop();
        const availableTime = nextStart - currentTime;
        if (availableTime >= stackLeftTime) {
          answer.push(stackName);
          currentTime += stackLeftTime;
        } else {
          // 이전 수행중이던 과제를 수행하다가 다시 스택에 담는경우, 남은 시간을 업데이트 해야 합니다.
          stack.push([stackName, stackLeftTime - availableTime]);
          break;
        }
      }
    }
  }

  return answer;
}

const convertToMinute = (time) => {
  const [hour, minute] = time.split(':').map(Number);
  return hour * 60 + minute;
};
