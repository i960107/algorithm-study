from collections import deque

def BFS(start, graph, dq, visited):
    dq.append(start)
    visited[start] = True
    while dq:
        node = dq.popleft()
        for nxt in graph[node]:
            if not visited[nxt]:
                dq.append(nxt)
                visited[nxt] = True

def solution(n, computers):
    graph = [[] for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i + 1].append(j + 1)
    visited = [False] * (n + 1)
    dq = deque()
    cnt = 0
    for i in range(1, n + 1):
        # visited가 False이면 dq에 위치를 append하기
        if not visited[i]:
            dq.append(i)
            BFS(i, graph, dq, visited)
            cnt += 1
    return cnt
