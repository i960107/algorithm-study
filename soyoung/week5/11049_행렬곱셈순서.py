# 해인님의 풀이와 블로그 설명 참고했습니다!
# dp[i][j]: i행렬부터 j행렬까지의 최소 곱셈 연산 횟수
import sys
n = int(sys.stdin.readline())
nums = [list(map(int, input().split())) for i in range(n)]
dp = [[0]*n for _ in range(n)]

for d in range(1, n):   # d는 대각선
    for i in range(n-d):    # i는 행 (n-d개의 행)
        j = i + d       # j는 열  (i행 + d번째 대각선)

        dp[i][j] = float('inf')
        for k in range(i,j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + nums[i][0] * nums[k+1][0] * nums[j][1])

print(dp[0][-1])