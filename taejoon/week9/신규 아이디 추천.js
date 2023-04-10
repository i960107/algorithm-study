function solution(new_id) {
  const answer = '';

  // 1단계 - 4단계
  new_id = new_id
    .toLowerCase(new_id)
    .replace(/[^\w\d-_.]/g, '')
    .replace(/\.{2,}/g, '.')
    .replace(/^\.|\.$/g, '');

  // 5단계
  if (new_id.length === 0) new_id = 'a';
  // 6단계
  if (new_id.length >= 16) new_id = new_id.slice(0, 15);
  if (new_id[new_id.length - 1] === '.') new_id = new_id.slice(0, 14);

  // 7단계
  if (new_id.length <= 2) {
    let lastLetter = new_id[new_id.length - 1];
    while (new_id.length !== 3) {
      new_id += lastLetter;
    }
  }

  return new_id;
}
