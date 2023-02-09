import sys
from collections import deque
# visited 따져야 하는 이유? -> 단방향이긴 하지만 최단 거리를 구하므로!

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
distance = [-1 for _ in range(n+1)]  # 아직 방문 안했을 때 -1

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

def bfs(start_v):
    queue = deque()
    queue.append(start_v)

    while queue:
        v = queue.popleft()
        for j in graph[v]:
            if distance[j] == -1:
                distance[j] = 1 + distance[v]
                queue.append(j)

distance[x] = 0
bfs(x)

result = []
for i in range(1, n+1):
    if distance[i] == k:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    print(*result)
