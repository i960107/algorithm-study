from typing import List


def solution(n: int, stairs: List[int]) -> int:
    # 연속해서 3개를 안밟는 경우가 까다로움.
    # dp는 각 계단을 밟았을때 얻을 수 있는 최대 점수
    # 계단이 3개보다 적은 경우 주의!
    if n == 1:
        return stairs[0]
    elif n == 2:
        return stairs[0] + stairs[1]
    elif n == 3:
        return max(stairs[0], stairs[1]) + stairs[2]

    dp = [0] * (n + 1)
    dp[1] = stairs[0]
    dp[2] = stairs[0] + stairs[1]
    dp[3] = max(stairs[0], stairs[1]) + stairs[2]
    k = 3
    while k < n:
        k += 1
        dp[k] = (max(dp[k - 3] + stairs[k - 2], dp[k - 2]) + stairs[k - 1])
    return dp[n]


n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))

print(solution(n, stairs))
