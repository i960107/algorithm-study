# sol1. dfs 재귀 풀이 (실패)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
computers = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def dfs(v, cnt, start_v, test_visited):
    test_visited[v] = True

    for i in graph[v]:
        if not test_visited[i]:
            computers[start_v] = cnt + 1
            dfs(i, cnt + 1, start_v, test_visited)


for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    dfs(i, 1, i, visited)

most = max(computers)
result = []

for i in range(1, n+1):
    if computers[i] == most:
        result.append(i)

print(*result)
