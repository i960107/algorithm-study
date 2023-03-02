import sys
input = sys.stdin.readline

t = int(input())

from collections import deque


def bfs(start, plane):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        # 국가를 모두 방문하면
        if visited.count(True) == n:
            return plane

        curr = q.popleft()

        for node in graph[curr]:
            if not visited[node]:
                q.append(node)
                plane += 1
                visited[node] = True

for _ in range(t):
    n,m = map(int, input().split())
    # n개의 국가를 모두 방문했는가
    visited = [False] * (n+1)

    graph = [[] for _ in range(n+1)]

    for i in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    p = bfs(1,0)
    print(p)
