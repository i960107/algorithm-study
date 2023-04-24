function solution(n, build_frame) {
  const canDelete = (x, y, a, arr) => {
    const idx = arr.findIndex(
      ([px, py, pa]) => px === x && py === y && pa === a
    );
    const copy = [...arr];
    copy.splice(idx, 1);
    for (const [px, py, pa] of copy) {
      if (pa === 0) {
        if (
          py === 0 ||
          copy.some(
            ([cx, cy, ca]) =>
              (cx === px && cy === py - 1 && ca === 0) ||
              (cx === px - 1 && cy === py && ca === 1) ||
              (cx === px && cy === py && ca === 1)
          )
        ) {
          continue;
        }
        return false;
      } else {
        if (
          copy.some(
            ([cx, cy, ca]) =>
              (cx === px && cy === py - 1 && ca === 0) ||
              (cx === px + 1 && cy === py - 1 && ca === 0) ||
              (cx === px - 1 &&
                cy === py &&
                ca === 1 &&
                (copy.some(
                  ([cx2, cy2, ca2]) => cx2 === px + 1 && cy2 === py && ca2 === 1
                ) ||
                  x === px + 1)) ||
              (cx === px &&
                cy === py &&
                ca === 1 &&
                (copy.some(
                  ([cx2, cy2, ca2]) => cx2 === px - 1 && cy2 === py && ca2 === 1
                ) ||
                  x === px - 1))
          )
        ) {
          continue;
        }
        return false;
      }
    }
    return true;
  };

  const isValid = (x, y, a, arr) => {
    if (a === 0) {
      if (
        y === 0 ||
        arr.some(
          ([cx, cy, ca]) =>
            (cx === x && cy === y - 1 && ca === 0) ||
            (cx === x && cy === y && ca === 1) ||
            (cx === x - 1 && cy === y && ca === 1)
        )
      ) {
        return true;
      }
      return false;
    } else {
      if (
        arr.some(
          ([cx, cy, ca]) =>
            (cx === x && cy === y - 1 && ca === 0) ||
            (cx === x + 1 && cy === y - 1 && ca === 0) ||
            (cx === x - 1 && cy === y && ca === 1) ||
            (cx === x + 1 && cy === y && ca === 1)
        )
      ) {
        return true;
      }
      return false;
    }
  };

  const answer = [];
  for (const [x, y, a, b] of build_frame) {
    if (b === 1) {
      if (isValid(x, y, a, answer)) {
        answer.push([x, y, a]);
      }
    } else {
      if (canDelete(x, y, a, answer)) {
        const idx = answer.findIndex(
          ([px, py, pa]) => px === x && py === y && pa === a
        );
        answer.splice(idx, 1);
      }
    }
  }
  return answer.sort((a, b) => a[0] - b[0] || a[1] - b[1] || a[2] - b[2]);
}
