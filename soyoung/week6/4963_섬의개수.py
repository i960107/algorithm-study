import sys
from collections import deque
def BFS(a, b):
    dq = deque()
    dq.append((a,b))
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, 1, -1, -1]
    while dq:
        x, y = dq.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<h and 0<=ny<w:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    dq.append((nx, ny))

while True:
    w, h = map(int, sys.stdin.readline().split())
    ans = 0
    if w == 0 and h == 0:
        break
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                BFS(i,j)
                ans += 1
    print(ans)