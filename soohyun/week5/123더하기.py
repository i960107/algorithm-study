def solution(n: int) -> int:
    if n <= 2:
        return n
    elif n == 3:
        return 4

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    k = 3
    while k < n:
        k += 1
        dp[k] = dp[k - 1] + dp[k - 2] + dp[k - 3]
    return dp[n]


n = int(input())
for _ in range(n):
    print(solution(int(input())))
