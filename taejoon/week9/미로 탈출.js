function solution(n, start, end, roads, traps) {
  let mincost = Number.MAX_VALUE;
  const costs = Array.from({ length: n + 1 }, () => ({}));

  const queue = [[start, '', 0]];
  while (queue.length) {
    const [node, state, cost] = queue.shift();

    for (const [from, to, weight] of roads) {
      if (from !== node) continue;

      const new_state = state.split('').map((v, i) => {
        if (traps[i] === from) return 1 - Number(v);
        else if (traps[i] === to) return 1 - Number(v);
        else return Number(v);
      });
      const new_state_str = new_state.join('');

      if (
        costs[to][new_state_str] === undefined ||
        costs[to][new_state_str] > cost + weight
      ) {
        if (cost + weight < mincost) {
          costs[to][new_state_str] = cost + weight;
          if (to === end) mincost = cost + weight;
          else queue.push([to, new_state_str, cost + weight]);
        }
      }
    }
  }

  return mincost;
}
