import sys
from collections import deque

# 키 작은 학생이 먼저
def topolopy_sort(graph, indegree):
    result = []
    dq = deque()
    for node in range(1, n+1):
        if indegree[node] == 0:
            dq.append(node)
    while dq:
        now = dq.popleft()
        result.append(now)
        for nx in graph[now]:
            indegree[nx] -= 1
            if indegree[nx] == 0:
                dq.append(nx)
    print(*result)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1
topolopy_sort(graph, indegree)