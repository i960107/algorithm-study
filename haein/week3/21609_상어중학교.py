import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))

block_group = []
move = [(-1, 0), (0, 1), (1, 0), (0. -1)]

def group(x, y):
    queue = deque([(x, y)])
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[x][y] = True

    while queue:
        curx, cury = queue.popleft()

        for dx, dy in move:
            mx, my = curx + dx, cury + dy
            if 0 <= mx <= n-1 and 0 <= my <= n-1:
                if graph[mx][my] != -1:
                    block_group.append() # 일반 블럭의 색깔이 같은 거끼리 어떻게 모을 수 있을까? 2개 이상인 것들만 어떻게 모을까?


group(0, 0)


