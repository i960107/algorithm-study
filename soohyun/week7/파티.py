from typing import List
from sys import stdin

read = stdin.readline
INF = int(1e9)
N, M, X = map(int, input().split())

# 플루이드-워셜 풀이
# # 갈수 없는 것과 distance과 0인(자기자신에게 가는 경우)는 구분 해줘야함.
dp = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][i] = 0

# 단방향이기 때문에 오고 가는 길이 다름
# dp[i][x] != dp[x][i]
for _ in range(M):
    a, b, t = map(int, read().split())
    dp[a][b] = t

# 시간 초과. O(N^3) = 1,000,000,000
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if dp[a][k] + dp[k][b] < dp[a][b]:
                dp[a][b] = dp[a][k] + dp[k][b]

        # dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])

max_distance = 0
for student in range(1, N + 1):
    if dp[student][X] + dp[X][student] > max_distance:
        max_distance = dp[student][X] + dp[X][student]

print(max_distance)

# OELogV * V => 10,000 * 10 * 1,000거의 비슷한데...
