from collections import deque

n = int(input())
result = []
visited = [0 for i in range(n+1)]
def bfs(v, visited):
    queue = deque([[v]])
    visited[v] = 1

    while queue:
        v = queue.popleft() # [5]
        t = v[0] # 5
        visited[t] = 1

        if t == 1:
            return v

        if t % 3 == 0 and visited[t // 3] == 0:
            queue.append([t//3] + v)
        if t % 2 == 0 and visited[t // 2] == 0:
            queue.append([t//2] + v)
        if visited[t - 1] == 0:
            queue.append([t-1] + v) # [4, 5]

res = bfs(n, visited)

print(len(res) - 1)
print(*res[::-1])



'''
처음엔 DFS를 사용하려고 했으나, 이렇게 하면 최단거리가 나오지 않음..
BFS는 같은 레벨의 자식 노드들의 탐색 깊이가 같으므로 최단 경로를 찾을 때 유리하다.

def dfs(v, visited, tmp):
    visited[v] = 1
    tmp.append(v)

    if v == 1:
        result.append(tmp)
        return

    if v % 3 == 0 and visited[v // 3] == 0:
        dfs(v//3, visited, tmp)
    if v % 2 == 0 and visited[v // 2] == 0:
        dfs(v//2, visited, tmp)
    if visited[v - 1] == 0:
        dfs(v-1, visited, tmp)

dfs(n, visited = [0 for i in range(n + 1)], tmp = [])

print(result)
'''
