import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(s, x, y, v, w, h):
    move = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    v[x][y] = 1

    for mx, my in move:
        nx, ny = x + mx, y + my
        if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == 1 and v[nx][ny] == 0:
            dfs(s, nx, ny, v, w, h)
    return v

def solution(s, w, h):
    visited = [[0 for _ in range(w)] for _ in range(h)]
    answer = 0

    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and s[i][j] == 1:
                visited = dfs(s, i, j, visited, w, h)
                answer += 1
            else:
                continue

    return answer


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
    else:
        square = [[] for _ in range(h)]
        for i in range(h):
            square[i] = list(map(int, input().split()))
        print(solution(square, w, h))
