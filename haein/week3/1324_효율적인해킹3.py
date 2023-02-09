# sol3. bfs 풀이
# bfs에서 각 시작점마다 걀 수 있는 곳 다 돌고 cnt 리턴
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start_v):
    queue = deque()
    queue.append(start_v)
    cnt = 1
    visited = [False for _ in range(n+1)]
    visited[start_v] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]: # 큐에 방문하기 전에 확인 -> 큐에 넣은 거 자체가 방문 한 것
                cnt += 1
                visited[i] = True
                queue.append(i)
    return cnt

comp = -1
result = []

for i in range(1, n+1):
    tmp = bfs(i)
    if tmp > comp:
        comp = tmp
        result = [i]
    elif tmp == comp:
        result.append(i)

print(*result)


# 시간초과 <- why?
def bfs(start_v):
    queue = deque()
    queue.append(start_v)
    cnt = 0
    visited = [False for _ in range(n+1)]

    while queue:
        v = queue.popleft()

        if visited[v]: # 큐에서 뺀 이후에 visited 처리 -> 큐에서 빠질 때 방문하는 것
            continue

        cnt += 1
        visited[v] = True

        for i in graph[v]:
            if not visited[i]:
                cnt += 1
                queue.append(i)
    return cnt
