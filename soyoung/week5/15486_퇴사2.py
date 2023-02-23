import sys
n = int(sys.stdin.readline())
board = [(0, 0) for _ in range(n+1)]
for i in range(1, n+1):
    board[i] = tuple(map(int, sys.stdin.readline().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = max(dp[i], dp[i-1])
    fin_date = i + board[i][0] - 1
    if fin_date <= n:
        dp[fin_date] = max(dp[fin_date], dp[i-1] + board[i][1])
print(max(dp))