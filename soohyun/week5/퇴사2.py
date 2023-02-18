from sys import stdin
from typing import List, Tuple


def solution(n: int, pay: List[Tuple[int, int]]) -> int:
    # 전날까지 벌 수 있는 최대 금액
    dp = [0] * (n + 2)
    for day, (t, p) in enumerate(pay, 1):
        dp[day] = max(dp[day - 1], dp[day])
        if day + t <= n + 1:
            dp[day + t] = max(dp[day + t], dp[day] + p)

    # 왜 max를 해줘야하는지 조금 헷갈림.
    return max(dp[n], dp[n + 1])


n = int(input())
pay = []
input = stdin.readline
for _ in range(n):
    t, p = map(int, input().split())
    pay.append((t, p))
print(solution(n, pay))
