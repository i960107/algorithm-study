import sys
from collections import deque
# 트리의 지름은 DFS를 2번 실행
def DFS(start):
    visited = [False] * (n+1)
    dq = deque()
    dq.append((start, 0))
    while dq:
        cur, dist = dq.popleft()
        visited[cur] = True
        for nxt, ndist in graph[cur]:
            if not visited[nxt]:
                if dist+ndist > distance[nxt]:
                    distance[nxt] = dist+ndist
                    dq.append((nxt, dist+ndist))

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, w = map(int, sys.stdin.readline().split())
    graph[a].append((b, w))
    graph[b].append((a, w))
distance = [0] * (n+1)
DFS(1)
node = distance.index(max(distance))
distance = [0] * (n+1)
DFS(node)
print(max(distance))
