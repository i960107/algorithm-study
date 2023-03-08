from sys import stdin
import heapq
from collections import defaultdict
from typing import Dict, List

read = stdin.readline
INF = int(1e9)
N, M, X = map(int, input().split())


# 플루이드-워셜 풀이
# # 갈수 없는 것과 distance과 0인(자기자신에게 가는 경우)는 구분 해줘야함.
# dp = [[INF] * (N + 1) for _ in range(N + 1)]
#
# for i in range(1, N + 1):
#     dp[i][i] = 0
#
# # 단방향이기 때문에 오고 가는 길이 다름
# # dp[i][x] != dp[x][i]
# for _ in range(M):
#     a, b, t = map(int, read().split())
#     dp[a][b] = t
#
# # 시간 초과. O(N^3) = 1,000,000,000
# for k in range(1, N + 1):
#     for a in range(1, N + 1):
#         for b in range(1, N + 1):
#             if dp[a][k] + dp[k][b] < dp[a][b]:
#                 dp[a][b] = dp[a][k] + dp[k][b]
#
#         # dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])
#
# max_distance = 0
# for student in range(1, N + 1):
#     if dp[student][X] + dp[X][student] > max_distance:
#         max_distance = dp[student][X] + dp[X][student]
#
# print(max_distance)

# 다익스트라로하면 뭐가 다른가..
# OELogV * V => 10,000 * 10 * 1,000거의 비슷한데...

def dijkstra(adj: Dict[int, List], start: int) -> List[int]:
    distance = [INF for _ in range(N + 1)]
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        acc_dist, curr = heapq.heappop(queue)

        if distance[curr] < acc_dist:
            continue

        for (next, dist) in adj[curr]:
            next_dist = acc_dist + dist
            if distance[next] > next_dist:
                distance[next] = next_dist
                heapq.heappush(queue, (next_dist, next))
    return distance


adj = defaultdict(list)
distances = [[INF] * (N + 1)]

for _ in range(M):
    a, b, t = map(int, read().split())
    adj[a].append((b, t))

for i in range(1, N + 1):
    distance = dijkstra(adj, i)
    distances.append(distance)

longest_distance = 0
for i in range(1, N + 1):
    if distances[i][X] + distances[X][i] > longest_distance:
        longest_distance = distances[i][X] + distances[X][i]

print(longest_distance)
