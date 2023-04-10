from sys import stdin

read = stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에게 가는 비용
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, read().split())
    graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            # 음의 간선 포함가능. 자기 자신에게 가는 길, 인접한 노드의 경우에도 값 갱신될 수 있음
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == 'INF':
            print("INFINITY", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
