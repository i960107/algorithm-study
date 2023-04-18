from typing import List
from collections import defaultdict


def solution(sales: List[int], links: List[List[int]]) -> int:
    answer = 0

    n = len(sales)
    INF = int(1e9)
    dp = [[INF, INF] for _ in range(n + 1)]

    teams = defaultdict(list)
    for u, v in links:
        teams[u].append(v)

    def dfs(n: int):
        if n not in teams:
            dp[n][0] = 0
            dp[n][1] = sales[n - 1]
            return

        children_total_sales = 0
        has_at_least_one = False
        min_diff = INF
        for member in teams[n]:
            dfs(member)
            # 참석하거나, 참석하지 않거나 매출액이 같다면?
            if dp[member][0] > dp[member][1]:
                children_total_sales += dp[member][1]
                has_at_least_one = True
            else:
                children_total_sales += dp[member][0]
            min_diff = min(min_diff, dp[member][1] - dp[member][0])
        dp[n][1] = sales[n - 1] + children_total_sales
        if has_at_least_one:
            dp[n][0] = children_total_sales
        # 만약 팀원중에 아무도 참석하지 않았다면, 참석시켰을때 가장 손실이 적은 팀원 참석시키기.
        # 참석시키는 비용 => dp[child][1] - dp[child][0]
        else:
            dp[n][0] = children_total_sales + min_diff

    dfs(1)
    print(dp)
    return min(dp[1][0], dp[1][1])


print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],
               [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))
