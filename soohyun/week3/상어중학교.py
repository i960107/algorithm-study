from collections import deque
from typing import List


# dr = (0, 1, 0, -1)
# dc = (1, 0, -1, 0)
# score = 0
# groups = [[0] * N for _ in range(N)]
# group_idx = 0
# sz = 0
# rainbow = 0
# block_color = 0
#
#
# def is_valid_coord(r, c):
#     return 0 <= r < N and 0 <= c < N
#
#
# def recur(r, c):
#     global sz, rainbow
#     for k in range(4):
#         nr = r + dr[k]
#         nc = c + dc[k]
#         if is_valid_coord(nr, nc) and groups[nr][nc] == 0:
#             if board[nr][nc] == 0:
#                 rainbow += 1
#             sz += 1
#             groups[nr][nc] = group_idx
#             recur(nr, nc)
#
#
# def recur_remove(r, c):
#     for k in range(4):
#         nr = r + dr[k]
#         nc = c + dc[k]
#         if is_valid_coord(nr, nc) and board[nr][nc] >= 0 and (board[nr][nc] == 0 or groups[nr][nc] == group_idx):
#             board[nr][nc] = -1
#             recur_remove(nr, nc)
#
#
# def pull_down():
#     for j in range(N):
#         for i in range(N - 1, -1, -1):
#             if board[i][j] == -1:
#                 for k in range(i - 1, -1, -1):
#                     if board[k][j] == -1:
#                         break
#

class Group:
    def __init__(self, group_idx: int, color: int, size: int, rainbows: int, r: int, c: int):
        self.idx = group_idx
        self.color = color
        self.size = size
        self.rainbows = rainbows
        self.r = r
        self.c = c


# 그룹 별 사이즈, 기준 블록, 무지개 블록 갯수 기록해야 하는 것 아닌가?


def is_valid_coord(r: int, c: int) -> bool:
    if 0 <= r < N and 0 <= c < N:
        return True
    return False


def bfs(r: int, c: int):
    dr = (0, 0, 1, -1)
    dc = (1, -1, 0, 0)

    block_color = board[r][c]
    global groups
    groups += 1

    group_size = 1
    rainbow = 0

    queue = deque()
    queue.append((r, c))
    visited[r][c] = True

    while queue:
        cr, cc = queue.popleft()

        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if is_valid_coord(nr, nc) and board[nr][nc] in (block_color, 0) and not visited[nr][nc]:
                group_size += 1

                if board[cr][cc] == 0:
                    rainbow += 1
                queue.append((nr, nc))
                visited[nr][nc] = True

    if group_size < 2:
        return

    group_info[groups] = Group(groups, block_color, group_size, rainbow, r, c)


def pull_down():
    # 어떻게 처리하지. 점수를.
    for c in range(N):
        start = N - 1
        while start >= 0:
            numbers = deque()
            next_start = start
            for r in range(start, -1, -1):
                next_start -= 1
                if board[r][c] == -1:
                    break
                if board[r][c] is not None:
                    numbers.append(board[r][c])
                    board[r][c] = None

            for r in range(start, -1, -1):
                if len(numbers) == 0:
                    break
                board[r][c] = numbers.popleft()
            start = next_start


# pull left만 해서는 안됨 반시계 방향으로 돌려야 검은 블록의 위치가 변함.
def rotate():
    rotated = [[None] * N for _ in range(N)]
    nr, nc = 0, 0
    global board
    for c in range(N - 1, -1, -1):
        for r in range(N):
            rotated[nr][nc] = board[r][c]
            nc += 1
        nr += 1
        nc = 0
    board = rotated


def pop_blocks() -> int:
    target = None
    for idx, info in group_info.items():
        if not target:
            target = info
            continue
        if target.size > info.size:
            continue
        if target.size < info.size:
            target = info
            continue
        if target.rainbows > info.rainbows:
            continue
        if target.rainbows < info.rainbows:
            target = info
            continue
        target = info

    dr = (0, 0, 1, -1)
    dc = (1, -1, 0, 0)

    queue = deque()
    queue.append((target.r, target.c))
    popped = 1
    board[target.r][target.c] = None

    while queue:
        cr, cc = queue.popleft()

        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if is_valid_coord(nr, nc) and board[nr][nc] in (0, target.color):
                popped += 1
                board[nr][nc] = None
                queue.append((nr, nc))

    return popped


N, colors = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

total_score = 0
while True:
    visited = [[False] * N for _ in range(N)]
    # {영역번호: Group 객체}
    group_info = dict()
    # group cnt -> 영역 번호
    groups = 0

    for r in range(N):
        for c in range(N):
            if board[r][c] in (-1, 0) or visited[r][c]:
                continue
            bfs(r, c)

    score = pop_blocks() ** 2
    if score == 0:
        break
    total_score += score
    pull_down()
    rotate()
    pull_down()

print(total_score)
