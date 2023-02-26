from typing import List


def solution(n: int) -> List[int]:
    dp = [0] * (n + 1)
    for i in range(n + 1):
        # 겹치면?
        dp[i] += dp[i % 3]
        dp[i] += dp[i % 2]
        dp[i] += dp[i - 2]


n = int(input())
res = solution(n)
print(len(res))
print(*res)
