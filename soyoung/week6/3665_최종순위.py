import sys
from collections import deque

def topolopy_sort(graph, indegree):
    result = []
    dq = deque()
    for node in range(1,n+1):
        if indegree[node] == 0:
            dq.append(node)
    while dq:
        now = dq.popleft()
        result.append(now)
        for nx in graph[now]:
            indegree[nx] -= 1
            if indegree[nx] == 0:
                dq.append(nx)
    if len(result) < n:
        print('IMPOSSIBLE')
    else:
        print(*result)

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for i in range(n):
        for j in range(i+1,n):
            graph[array[i]].append(array[j])
            indegree[array[j]] += 1

    m = int(sys.stdin.readline())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        # b -> a 인 경우 a -> b로 변경
        if a in graph[b]:
            graph[b].remove(a)
            graph[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1
        elif b in graph[a]:
            graph[a].remove(b)
            graph[b].append(a)
            indegree[b] -= 1
            indegree[a] += 1
    topolopy_sort(graph, indegree)