import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)] # 보드 : 사과 1, 없음 0

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    board[b-1][a-1] = 1 # 계속 실수 했던 부분!!! a행 b열이면 a가 y축 좌표이고 b가 x축 좌표!

d = int(input())
dir = dict() # 방향 변경
for _ in range(d):
    a, b = input().split()
    dir[int(a)] = b

body = deque([(0,0)]) # 몸

move = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 이동 시 방향
cur_x, cur_y = 0, 0 # 현재 머리의 위치
idx = 0 # 이동 시 인덱스
time = 0 # 현재 시간

while True:
    time += 1

    nx, ny = cur_x + move[idx][0], cur_y + move[idx][1]

    if 0 > nx or nx >= n or 0 > ny or ny >= n:
        break
    if (nx, ny) in body:
        break

    body.append((nx, ny))

    if board[nx][ny] == 1:
        board[nx][ny] = 0
    else:
        body.popleft()

    cur_x, cur_y = nx, ny

    if time in dir.keys():
        if dir[time] == 'D':
            idx = (idx + 1) % 4
        else:
            idx = (idx - 1) % 4

print(time)
