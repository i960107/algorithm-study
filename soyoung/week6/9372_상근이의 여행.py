import sys
from collections import deque
# deque 사용해서 풀이
t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    # graph, visited 생성
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n + 1)
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    dq = deque()
    dq.append(1)
    visited[1] = True
    cnt = 0
    while dq:
        node = dq.popleft()
        for nx in graph[node]:
            # 아직 방문하지 않은 노드라면
            if not visited[nx]:
                visited[nx] = True
                cnt += 1
                dq.append(nx)
    print(cnt)