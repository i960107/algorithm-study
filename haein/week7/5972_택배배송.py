import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heappop(q)

        if distance[now] < dist:
            continue

        for b, c in graph[now]:
            cost = dist + c
            if cost < distance[b]:
                distance[b] = cost
                heappush(q, (cost, b))

dijkstra(1)

print(distance[n])
