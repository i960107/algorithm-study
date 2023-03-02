import sys
from collections import deque
def BFS(a, b):
    dq = deque()
    dq.append((a, b))
    dr = [(1, 0), (0, 1)]
    while dq:
        x, y = dq.popleft()
        if x == n-1 and y == m-1:
            break
        for r in dr:
            nx = x + r[0]
            ny = y + r[1]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    dq.append((nx, ny))
                else:
                    dq.append((nx, ny))

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            BFS(i,j)
            cnt += 1
print(cnt)