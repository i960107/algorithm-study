from sys import stdin

import heapq
from collections import defaultdict

read = stdin.readline
N, M = map(int, read().split())

# 어떻게 최소 값을 저장해주지
# n * n 행렬에 저장하면 매번 50,000번 탐색해야 하는데...
# 꼭 최소값 저장해주지 않아도 됨. heapq에서 heappop()할때 걸러짐.
INF = int(1e9)
adj = defaultdict(lambda: defaultdict(lambda: INF))
for _ in range(M):
    a, b, c = map(int, read().split())
    if c < adj[a][b]:
        adj[a][b] = c
        adj[b][a] = c

queue = [(0, 1)]
distance = [INF] * (N + 1)

while queue:
    dist, now = heapq.heappop(queue)

    if distance[now] < dist:
        continue

    for nxt, cost in adj[now].items():
        nxt_dist = dist + cost

        if distance[nxt] <= nxt_dist:
            continue
        distance[nxt] = nxt_dist
        heapq.heappush(queue, (nxt_dist, nxt))

print(distance[N])
