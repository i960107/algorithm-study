# sol2. bfs 풀이
# 시간 초과
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
computers = [0 for _ in range(n+1)]  # 자신 제외하고 해킹할 수 있는 수

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start_v):
    queue = deque()
    queue.append(start_v)
    start = start_v
    visited = [False for _ in range(n+1)]

    while queue:
        v = queue.popleft()
        visited[v] = True

        for i in graph[v]:
            if not visited[i]:
                computers[start] += 1
                queue.append(i)


for i in range(1, n+1):
    bfs(i)

big = -1

for i in range(len(computers)):
    if computers[i] > big:
        big = computers[i]

result = []
for i in range(len(computers)):
    if computers[i] == big:
        result.append(i)

print(*result)
