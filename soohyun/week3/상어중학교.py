from typing import List

N, colors = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)
score = 0
groups = [[0] * N for _ in range(N)]
group_idx = 0
sz = 0
rainbow = 0
block_color = 0


def is_valid_coord(r, c):
    return 0 <= r < N and 0 <= c < N


def recur(r, c):
    global sz, rainbow
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if is_valid_coord(nr, nc) and groups[nr][nc] == 0:
            if board[nr][nc] == 0:
                rainbow += 1
            sz += 1
            groups[nr][nc] = group_idx
            recur(nr, nc)

def recur_remove(r,c):
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if is_valid_coord(nr, nc) and board[nr][nc] >= 0 and (board[nr][nc] == 0 or groups[nr][nc] == group_idx):
            board[nr][nc] = -1
            recur_remove(nr, nc)

def pull_down():
    for j in range(N):
        for i in range(N-1, -1, -1):
            if board[i][j] == -1:
                for k in range(i-1, -1, -1):
                    if board[k][j] == -1:
                        break
