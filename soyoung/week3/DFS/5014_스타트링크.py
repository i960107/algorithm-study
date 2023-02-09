import sys
from collections import deque

def BFS(start):
    dq = deque()
    dq.append(start)
    visited = [-1] * (F+1)
    visited[start] = 0
    while dq:
        x = dq.popleft()
        if x == G:
            return visited[x]
        for nx in (x + U, x - D):
            if 0 <= nx <= F and visited[nx] == -1:
                dq.append(nx)
                visited[nx] = visited[x] + 1

    return "use the stairs"

F, S, G, U, D = map(int, sys.stdin.readline().split())
print(BFS(S))
