function canInstallPillar(x, y, pillars, bars) {
  if (y === 0) return true;
  if (pillars.has(`${x},${y - 1}`)) return true;
  if (bars.has(`${x - 1},${y}`) || bars.has(`${x},${y}`)) return true;
  return false;
}

function canInstallBar(x, y, pillars, bars) {
  if (pillars.has(`${x},${y - 1}`) || pillars.has(`${x + 1},${y - 1}`))
    return true;
  if (bars.has(`${x - 1},${y}`) && bars.has(`${x + 1},${y}`)) return true;
  return false;
}

function canRemove(pillars, bars, x, y) {
  const target = `${x},${y}`;
  if (pillars.has(target)) {
    pillars.delete(target);
    const ps = [...pillars];
    const bs = [...bars];
    for (const [px, py] of ps) {
      if (!canInstallPillar(px, py, pillars, bars)) {
        pillars.add(target);
        return false;
      }
    }
    for (const [bx, by] of bs) {
      if (!canInstallBar(bx, by, pillars, bars)) {
        pillars.add(target);
        return false;
      }
    }
    return true;
  }
  if (bars.has(target)) {
    bars.delete(target);
    const ps = [...pillars];
    const bs = [...bars];
    for (const [px, py] of ps) {
      if (!canInstallPillar(px, py, pillars, bars)) {
        bars.add(target);
        return false;
      }
    }
    for (const [bx, by] of bs) {
      if (!canInstallBar(bx, by, pillars, bars)) {
        bars.add(target);
        return false;
      }
    }
    return true;
  }
  return false;
}

function solution(n, build_frame) {
  let pillars = new Set();
  let bars = new Set();
  for (const [x, y, a, b] of build_frame) {
    if (b === 1) {
      if (a === 0 && canInstallPillar(x, y, pillars, bars)) {
        pillars.add(`${x},${y}`);
      } else if (a === 1 && canInstallBar(x, y, pillars, bars)) {
        bars.add(`${x},${y}`);
      }
    } else {
      if (a === 0 && canRemove(pillars, bars, x, y)) {
        pillars.delete(`${x},${y}`);
      } else if (a === 1 && canRemove(pillars, bars, x, y)) {
        bars.delete(`${x},${y}`);
      }
    }
  }

  pillars = [...pillars].map((v) => v + ',0');
  bars = [...bars].map((v) => v + ',1');
  const answer = [...pillars, ...bars].map((pos) => pos.split(',').map(Number));
  return answer.sort((a, b) => {
    if (a[0] !== b[0]) return a[0] - b[0];
    if (a[1] !== b[1]) return a[1] - b[1];
    return a[2] - b[2];
  });
}

function canInstallPillar(x, y, pillars, bars) {
  if (y === 0) return true;
  if (pillars.has(`${x},${y - 1}`)) return true;
  if (bars.has(`${x - 1},${y}`) || bars.has(`${x},${y}`)) return true;
  return false;
}

function canInstallBar(x, y, pillars, bars) {
  if (pillars.has(`${x},${y - 1}`) || pillars.has(`${x + 1},${y - 1}`))
    return true;
  if (bars.has(`${x - 1},${y}`) && bars.has(`${x + 1},${y}`)) return true;
  return false;
}

function canRemove(pillars, bars, x, y) {
  const target = `${x},${y}`;
  let isPillar = false,
    isBar = false;
  if (pillars.has(target)) {
    pillars.delete(target);
    isPillar = true;
  }
  if (bars.has(target)) {
    bars.delete(target);
    isBar = true;
  }

  const ps = [...pillars];
  const bs = [...bars];
  for (const [px, py] of ps) {
    if (!canInstallPillar(px, py, pillars, bars)) {
      if (isPillar) pillars.add(target);
      if (isBar) bars.add(target);
      return false;
    }
  }
  for (const [bx, by] of bs) {
    if (!canInstallBar(bx, by, pillars, bars)) {
      if (isPillar) pillars.add(target);
      if (isBar) bars.add(target);
      return false;
    }
  }
  return true;
}

function solution(n, build_frame) {
  let pillars = new Set();
  let bars = new Set();
  for (const [x, y, a, b] of build_frame) {
    if (b === 1) {
      if (a === 0 && canInstallPillar(x, y, pillars, bars)) {
        pillars.add(`${x},${y}`);
      } else if (a === 1 && canInstallBar(x, y, pillars, bars)) {
        bars.add(`${x},${y}`);
      }
    } else {
      if (a === 0 && canRemove(pillars, bars, x, y)) {
        pillars.delete(`${x},${y}`);
      } else if (a === 1 && canRemove(pillars, bars, x, y)) {
        bars.delete(`${x},${y}`);
      }
    }
  }

  const answer = [];
  for (const p of pillars) {
    const [x, y] = p.split(',').map(Number);
    answer.push([x, y, 0]);
  }
  for (const b of bars) {
    const [x, y] = b.split(',').map(Number);
    answer.push([x, y, 1]);
  }
  return answer.sort((a, b) => {
    if (a[0] !== b[0]) return a[0] - b[0];
    if (a[1] !== b[1]) return a[1] - b[1];
    return;
  });
}

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
        for (const [px, py, pa] of answer) {
          if (!isValid(px, py, pa, answer)) {
            answer.push([x, y, a]);
            break;
          }
        }
      }
    }
  }
  return answer.sort((a, b) => a[0] - b[0] || a[1] - b[1] || a[2] - b[2]);
}
