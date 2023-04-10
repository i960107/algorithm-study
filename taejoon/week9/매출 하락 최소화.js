function solution(sales, links) {
  let teams = new Map();
  for (let link of links) {
    if (teams.has(link[0])) {
      teams.set(link[0], [...teams.get(link[0]), link[1]]);
    } else {
      teams.set(link[0], [link[1]]);
    }
  }

  const dp = Array.from({ length: sales.length + 1 }, () => [0, 0]);

  const dfs = (node) => {
    if (teams.has(node)) {
      for (let child of teams.get(node)) {
        dfs(child);
        dp[node][0] += dp[child][1];
        dp[node][1] += Math.min(dp[child][0], dp[child][1]);
      }
    }

    dp[node][1] += sales[node - 1];
  };

  dfs(1);
  return Math.min(dp[1][0], dp[1][1]);
}
