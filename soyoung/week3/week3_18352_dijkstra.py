import sys
import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0
    while q:
        now, dist = heapq.heappop(q)
        if dist > distance[now]: continue
        for nx in graph[now]:
            if dist + 1 < distance[nx]:
                distance[nx] = dist + 1
                heapq.heappush(q, (nx, dist + 1))

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
INF = 1e8
distance = [INF] * (n+1)
dijkstra(x)
ans = []
for i in range(1, n+1):
    if distance[i] == k:
        ans.append(i)
if not ans: print(-1)
else:
    for i in ans:
        print(i)
