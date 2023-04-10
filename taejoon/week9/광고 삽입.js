function solution(play_time, adv_time, logs) {
  const playTime = convertToSeconds(play_time);
  const advTime = convertToSeconds(adv_time);
  const timeTable = new Array(playTime + 1).fill(0);

  logs.forEach((log) => {
    const [start, end] = log.split('-');
    const startTime = convertToSeconds(start);
    const endTime = convertToSeconds(end);

    timeTable[startTime] += 1;
    timeTable[endTime] -= 1;
  });

  for (let i = 1; i < timeTable.length; i++) {
    timeTable[i] += timeTable[i - 1];
  }

  for (let i = 1; i < timeTable.length; i++) {
    timeTable[i] += timeTable[i - 1];
  }

  let maxTime = 0;
  let maxTimeIndex = 0;

  for (let i = 0; i + advTime <= playTime; i++) {
    const time = timeTable[i + advTime] - timeTable[i];

    if (time > maxTime) {
      maxTime = time;
      maxTimeIndex = i + 1;
    }
  }
  return maxTimeIndex === 1 ? '00:00:00' : convertToTime(maxTimeIndex);
}

function convertToSeconds(time) {
  const [hour, minute, second] = time.split(':');

  return parseInt(hour) * 3600 + parseInt(minute) * 60 + parseInt(second);
}

function convertToTime(seconds) {
  const hour = Math.floor(seconds / 3600);
  const minute = Math.floor((seconds % 3600) / 60);
  const second = seconds % 60;

  return `${hour.toString().padStart(2, '0')}:${minute
    .toString()
    .padStart(2, '0')}:${second.toString().padStart(2, '0')}`;
}
