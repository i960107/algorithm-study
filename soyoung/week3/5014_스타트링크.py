import sys
from collections import deque

def BFS(start):
    dq = deque()
    dq.append(start)
    visited = [-1] * (F+1)
    visited[start] = 0
    while dq:
        now = dq.popleft()
        if now == G:
            return visited[now]
        for nx in (now+U, now-D):
            if 1 <= nx <= F and visited[nx] == -1:
                visited[nx] = visited[now] + 1
                dq.append(nx)
    return 'use the stairs'

F, S, G, U, D = map(int, sys.stdin.readline().split())
print(BFS(S))
