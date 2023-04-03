function solution(s) {
  const words = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
  ];
  const map = {
    zero: '0',
    one: '1',
    two: '2',
    three: '3',
    four: '4',
    five: '5',
    six: '6',
    seven: '7',
    eight: '8',
    nine: '9',
  };
  for (let word of words) {
    let k = s.indexOf(word);
    while (k !== -1) {
      s = s.slice(0, k) + map[word] + s.slice(k + word.length);
      k = s.indexOf(word);
    }
  }
  return Number(s);
}
