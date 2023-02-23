from sys import stdin
from typing import List, Tuple


def solution(n: int, pay: List[Tuple[int, int]]) -> int:
    # 전날까지 벌 수 있는 최대 금액
    dp = [0] * (n + 2)
    for day, (t, p) in enumerate(pay, 1):
        dp[day] = max(dp[day - 1], dp[day])
        if day + t <= n + 1:
            dp[day + t] = max(dp[day + t], dp[day] + p)

    # 전날까지 벌 수 있는 최대 금액을 기록했고, 마지막 인덱스의 경우 최대값으로 갱신이 안되므로 비교 필요
    return max(dp[n], dp[n + 1])


def solution_best(n: int, pay: List[Tuple[int, int]]) -> int:
    # 그날까지 벌 수 있는 최대 금액
    dp = [0] * (n + 1)
    for day, (t, p) in enumerate(pay, 1):
        dp[day] = max(dp[day - 1], dp[day])
        if day + t - 1 <= n:
            dp[day + t - 1] = max(dp[day + t - 1], dp[day - 1] + p)

    return dp[n]


n = int(input())
pay = []
input = stdin.readline
for _ in range(n):
    t, p = map(int, input().split())
    pay.append((t, p))
print(solution_best(n, pay))
