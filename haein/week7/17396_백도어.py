import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = 100000 * 100000 + 1 # 처음에 int(1e9)로 했다가 안 됨 -> 안전한 건 sys.maxsize인 듯!

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
possible = [0] + list(map(int, input().split()))

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a+1].append((b+1, t)) # 실수 안 하려면 이렇게 인덱스 번호와 맞춰주는 게 편할 것 같음
    graph[b+1].append((a+1, t))

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heappop(q)

        if distance[now] < dist:
            continue

        for b, t in graph[now]:
            cost = dist + t
            if possible[b] == 0 and b != n and cost < distance[b]:
                distance[b] = cost
                heappush(q, (cost, b))
            elif b == n and cost < distance[b]:
                distance[b] = cost
                heappush(q, (cost, b))

dijkstra(1)

if distance[n] != INF:
    print(distance[n])
else:
    print(-1)
