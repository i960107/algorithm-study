import sys

n = int(input())
graph = [[] for _ in range(n)]
height = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    graph[i] = tmp
    height += tmp

rain = set(height)
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(rain, x, y, test_visited):
    stack = [(x, y)]
    test_visited[x][y] = 1  # 방문

    while stack:
        nx, ny = stack.pop()
        for dx, dy in move:
            ax, ay = nx + dx, ny + dy
            if 0 <= ax <= n-1 and 0 <= ay <= n-1:
                if test_visited[ax][ay] == -1 and graph[ax][ay] > rain:
                    test_visited[ax][ay] = 1
                    stack.append((ax, ay))

result = []

for k in range(0, max(rain) + 1):
    r = k
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and graph[i][j] > r:
                cnt += 1
                dfs(r, i, j, visited)
    result.append(cnt)


print(max(result))
