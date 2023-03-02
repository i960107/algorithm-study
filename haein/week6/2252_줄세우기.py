import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)] # n번째 인덱스에 있는 점에서 그 안에 있는 원소로 이동
inDegree =  [0 for _ in range(n+1)] # 진입 차수 관리

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

def topology_sort():
    result = []
    queue = deque([])

    # 진입차수가 0인 것을 큐에 넣음
    for i in range(1, n+1):
        if inDegree[i] == 0:
            queue.append(i)

    while queue:
        v = queue.popleft()
        result.append(v)

        for i in graph[v]:
            inDegree[i] -= 1
            if inDegree[i] == 0:
                queue.append(i)

    print(*result)

topology_sort()
