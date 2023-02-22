def solution(n: int) -> int:
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    k = 2
    while k < n:
        k += 1
        dp[k] = dp[k - 2] + dp[k - 1]
    return dp[n] % 10007


print(solution(int(input())))
