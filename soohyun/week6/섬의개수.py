from typing import List
from sys import stdin
from collections import deque


def solution(w: int, h: int, grid: List[List[int]]):
    count = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 1:
                bfs(r, c, grid)
                count += 1

    return count


def bfs(r: int, c: int, grid: List[List[int]]):
    dr = (0, 0, 1, -1, 1, 1, -1, -1)
    dc = (1, -1, 0, 0, 1, -1, 1, -1)

    queue = deque()
    queue.append((r, c))
    grid[r][c] = 0
    while queue:
        cr, cc = queue.popleft()
        for k in range(8):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                grid[nr][nc] = 0
                queue.append((nr, nc))


read = stdin.readline
while True:
    w, h = map(int, read().split())
    if w == h == 0:
        break
    grid = []
    for _ in range(h):
        grid.append(list(map(int, read().split())))
    print(solution(w, h, grid))
