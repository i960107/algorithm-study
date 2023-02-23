n = int(input())

# sol 1. 과 sol 2. 모두 시간 비슷하게 걸림

# sol 1. 상향식 (Tabulation)
dp = [0 for _ in range(n+1)]  # 2*n 까지의 경우의 수

answer = 0

if n <= 3:
    answer = n
else:
    dp[1], dp[2], dp[3] = 1, 2, 3  # 4 이상의 입력값이 주어졌을 땐 이렇게 dp에 값을 넣어주는 게 필요! <- 따로 넣어주는 게 쉬운 에
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    answer = dp.pop()

print(answer%10007)

# sol 2. 하향식 (재귀)
dp = [0 for _ in range(n+1)]

answer = 0

if n <= 3:
    answer = n
    print(answer % 10007)
else:
    dp[1], dp[2], dp[3] = 1, 2, 3

    def sol(dp, n):
        if n == 1 or n == 2 or n == 3:
            return dp[n]
        elif dp[n] != 0:
            return dp[n]
        else:
            dp[n] = sol(dp, n-1) + sol(dp, n-2)
            return dp[n]

    print(sol(dp, n) % 10007)
