# sol. 1
# 참고 코드 https://fre2-dom.tistory.com/232
import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]
distance = [-1 for _ in range(n+1)]  # 노드 1에서 index 노드까지 거리, -1이면 방문 안한 것 (방문여부 + 거리)
distance2 = [-1 for _ in range(n+1)]

for i in range(n-1):
    p, j, w = map(int, sys.stdin.readline().split())
    graph[p].append([j, w]) # p번째 행에 j 노드 연결, w 거리
    graph[j].append([p, w])

def dfs(v, w):
    for j, pw in graph[v]:
        if distance[j] == -1:  # 방문 안 했다면
            distance[j] = w + pw  # 지금까지의 w + v -> j 까지 가는 데 필요한 pw
            dfs(j, w + pw)

distance[1] = 0
dfs(1, 0)

leaf_node = distance.index(max(distance))

def dfs2(v, w):
    for j, pw in graph[v]:
        if distance2[j] == -1:  # 방문 안 했다면
            distance2[j] = w + pw  # 지금까지의 w + v -> j 까지 가는 데 필요한 pw
            dfs2(j, w + pw)

distance2[leaf_node] = 0
dfs2(leaf_node, 0)

print(max(distance2))


# sol. 2
import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]
distance = [-1 for _ in range(n+1)]  # 노드 1에서 index 노드까지 거리, -1이면 방문 안한 것 (방문여부 + 거리)

for i in range(n-1):
    p, j, w = map(int, sys.stdin.readline().split())
    graph[p].append([j, w]) # p번째 행에 j 노드 연결, w 거리
    graph[j].append([p, w]) # 무방향이므로 둘 다 왔다갔다 가능 -> visited 처리해서 한 번만 방문해야 하는 이유 (거리 구하는 것이므로)

def dfs(v, w):
    for j, pw in graph[v]:
        if distance[j] == -1:  # 방문 안 했다면
            distance[j] = w + pw  # 지금까지의 w + v -> j 까지 가는 데 필요한 pw
            dfs(j, w + pw)

distance[1] = 0
dfs(1, 0)

leaf_node = distance.index(max(distance))
distance = [-1 for _ in range(n+1)] # 이것만 다시 초기화해주면 방문 기록 리셋됨
distance[leaf_node] = 0
dfs(leaf_node, 0)

print(max(distance))
