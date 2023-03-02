# 풀이 참조
# 크눅스의 최적화

import sys
T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())   # n은 4
    nums = list(map(int,input().split()))
    dp = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(n-1):
        # 첫 부분누적합 입력하기
        dp[i][i+1] = nums[i] + nums[i+1]
        for j in range(i+2,n):    # 각 행에 나머지 부분합 입력
            dp[i][j] = dp[i][j-1] + nums[j]
    for v in range(2,n):    # v는 대각선, 2~3
        for i in range(n-v):
            j = i+v
            dp[i][j] += min([dp[i][k] + dp[k+1][j] for k in range(i,j)])    # i=2, j=4 -> k는 2~3/ i=1, j=4 -> k는 1~3

    print(dp[0][n-1])


# import sys
# T = int(sys.stdin.readline())
# for i in range(T):
#     n = int(sys.stdin.readline())   # n은 4
#     nums = list(map(int,input().split()))
#     dp = [[0]*(n+1) for _ in range(n+1)]
#     for i in range(1, n):
#         dp[i][i+1] = nums[i-1] + nums[i]
#         for j in range(i+2, n+1):
#             dp[i][j] = dp[i][j-1] + nums[j-1]
#
#     for d in range(2, n):   # d는 대각선, 2~3
#         for i in range(1, n-d): # i는 행, 1~2
#             j = i + d
#             dp[i][j] += min([dp[i][k] + dp[k+1][j] for k in range(i, j)])
#     print(dp)