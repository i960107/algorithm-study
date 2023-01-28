from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

dx = [1, 0]
dy = [0, 1]

print(graph)

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    answer = 0
    tmp = 0

    while queue:
        x, y = queue.popleft()

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                tmp += 1

            queue.append((nx, ny))

        if x == N-1 and y == M-1:
            answer = tmp

    return answer

print(bfs(0, 0))
