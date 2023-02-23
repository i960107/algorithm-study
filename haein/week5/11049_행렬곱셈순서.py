# 내가 구해야 하는 것 : 입력으로 주어진 행렬의 순서를 바꾸면 안 되고 주어진 순서 그대로 dp[1][3]을 구해야 한다.
# dp[i][j]가 의미하는 것 : i행렬부터 j행렬까지의 최소 곱셈 연산 횟수
# 예제로 보았을 때 i는 1, j는 3으로 고정됨

# 점화식 : dp[i][j] = min(dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1])
# 여기서 k는 i부터 j-1이하의 값

import sys
input = sys.stdin.readline
n = int(input())
s = [list(map(int, input().split())) for i in range(n)]
dp = [[0] * n for _ in range(n)]

# n이 6인 경우

for d in range(1, n): # d번째 대각선                      # d:1
    for i in range(n - d): # i: 행 (n-d개의 행)           # d가 1이면 대각선이 지나는 행은 총 5개
        j = i + d # j: 열 (i행 + d번째 대각선)            # 행이 하나 커질 때마다 열도 하나씩 같이 늘어남

        dp[i][j] = 2 ** 32
        for k in range(i, j):                            # k는 i와 j-1 중 하나 (dp[i][j]는 i부터 j번까지 행렬곱 중 최소 곱셈 횟수)
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + s[i][0] * s[k+1][0] * s[j][1])
print(dp[0][n - 1])
