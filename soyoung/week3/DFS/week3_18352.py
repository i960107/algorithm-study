import sys
from collections import deque

def BFS(start):
    q = deque()
    q.append(start)
    visited[start] = True
    distance[start] = 0
    ans = []
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == k:
                    ans.append(i)

    if not ans: print(-1)
    else:
        ans.sort()
        for i in ans:
            print(i)

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
distance = [0] * (n+1)
visited = [False] * (n+1)
BFS(x)

