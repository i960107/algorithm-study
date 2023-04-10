function solution(orders, course) {
  const sortedOrders = orders.map((order) => {
    let o = order.split('');
    o.sort();
    return o.join('');
  });
  const hash = new Map();
  const answer = [];
  for (const num of course) {
    let combinations = {};
    for (const order of sortedOrders) {
      const combies = getCombinations(order, num);
      for (let combi of combies) {
        combinations[combi] = (combinations[combi] || 0) + 1;
      }
    }
    let keys = Object.keys(combinations);
    let max = Math.max(...keys.map((key) => combinations[key]));
    if (max === 1) continue;
    answer.push(...keys.filter((key) => combinations[key] === max));
  }
  answer.sort();
  return answer;
}

function getCombinations(array, length) {
  const combinations = [];

  function generateCombination(start, combination) {
    if (combination.length === length) {
      combinations.push(combination.join(''));
      return;
    }
    for (let i = start; i < array.length; i++) {
      generateCombination(i + 1, combination.concat(array[i]));
    }
  }

  generateCombination(0, []);

  return combinations;
}
