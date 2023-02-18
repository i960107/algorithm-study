import sys
import copy
from collections import deque
n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dq = deque()

def BFS(a, b, h):
    test[a][b] = 0
    while dq:
        x, y = dq.popleft()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if test[nx][ny] > h:
                    test[nx][ny] = 0
                    dq.append((nx, ny))

# 높이가 h이하이면 물에 잠김
ans = 0
for h in range(1, 101):
    cnt = 0
    test = copy.deepcopy(board)
    for i in range(n):
        for j in range(n):
            if test[i][j] > h:
                dq.append((i,j))
                BFS(i,j,h)
                cnt += 1
    ans = max(ans, cnt)
print(ans)