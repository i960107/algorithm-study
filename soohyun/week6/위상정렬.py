from typing import List
from collections import deque, defaultdict

v, e = map(int, input().split())
indegree = [0] * (v + 1)
# 각 그래프에 연결된 간선 정보를 담기 위한 연결 리스트
graph = defaultdict(list)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

result = []
q = deque()

for i in range(1, v + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    curr = q.popleft()
    result.append(curr)

    for i in graph[curr]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(*result)
