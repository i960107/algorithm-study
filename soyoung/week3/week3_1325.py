from collections import deque
import sys

def BFS(start):
    cnt = 1
    visited = [False] * (n + 1)
    visited[start] = True
    dq = deque([start])
    while dq:
        node = dq.popleft()
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                dq.append(nxt)
                cnt += 1
    return cnt

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

ans = [0 for i in range(n+1)]
for i in range(1, n+1):
    cnt = BFS(i)
    ans[i] = cnt
max_cnt = max(ans)
for i in range(1, n+1):
    if max_cnt == ans[i]:
        print(i, end=' ')