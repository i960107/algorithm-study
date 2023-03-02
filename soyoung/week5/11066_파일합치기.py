# 시간초과 발생
# dp[i][j]: i부터 j까지의 최소 비용
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    dp = [[0] * n for _ in range(n)]
    for d in range(1, n):   # d는 대각선, d = 1
        for i in range(n-d):    # i는 행, 0~2
            j = i + d       # j는 열, i가 1증가할때마다 j도 1증가
            dp[i][j] = 2**32
            for k in range(i,j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + sum(nums[i:j+1]))
    print(dp[0][n-1])

# 풀이 참조
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    # DP[i][j] : i에서 j까지 합하는데 필요한 최소 비용
    # DP[i][k] + DP[k+1][j] + sum(A[i]~A[j])
    DP = [[0 for i in range(N + 1)] for _ in range(N + 1)]
    for i in range(2, N + 1):  # 부분 파일의 길이
        for j in range(1, N + 2 - i):  # 시작점
            DP[j][j + i - 1] = min([DP[j][j+k] + DP[j+k+1][j+i-1] for k in range(i-1)]) + (sum(nums[j-1:j+i-1]))

    print(DP[1][N])

