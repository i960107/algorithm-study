import sys
# dp로 풀이
n = int(sys.stdin.readline())
dp = [[0, []] for _ in range(n+1)]
dp[1][0] = 0
dp[1][1] = [1]
# 연산은 3가지: -1, *3, *2
for i in range(2, n+1):
    # dp[i][0]는 연산하는 횟수
    dp[i][0] = dp[i-1][0] + 1
    # dp[i][1]는 1을 N으로 만드는 과정에 포함되는 수
    dp[i][1] = dp[i-1][1] + [i]
    # 현재 연산횟수(dp[i][0])가 이전 연산횟수보다 크다면 -> 이전 연산횟수+1 로 갱신(최소값이므로)
    if i % 3 == 0 and dp[i][0] > dp[i//3][0] + 1:
        dp[i][0] = dp[i//3][0] + 1
        dp[i][1] = dp[i//3][1] + [i]
    if i % 2 == 0 and dp[i][0] > dp[i//2][0] + 1:
        dp[i][0] = dp[i // 2][0] + 1
        dp[i][1] = dp[i // 2][1] + [i]

print(dp[n][0])
print(*reversed(dp[n][1]))