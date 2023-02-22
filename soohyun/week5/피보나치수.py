def solution(n: int) -> int:
    k = 1
    dp = [0, 1]

    while k < n:
        k += 1
        dp.append(dp[k - 2] + dp[k - 1])

    return dp[n]


print(solution(10))
