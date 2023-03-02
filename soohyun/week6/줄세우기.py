from typing import List
from collections import deque, defaultdict
from sys import stdin

read = stdin.readline
N, M = map(int, input().split())

indegree = [0] * (N + 1)
d = defaultdict(list)

for _ in range(M):
    a, b = map(int, read().split())
    indegree[b] += 1
    d[a].append(b)

queue = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
result = []
# 줄세우는 모든 방법을 알 수 있을까?
while queue:
    curr = queue.popleft()
    result.append(curr)

    for next in d[curr]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

print(*result)
