import sys
n, m = list(map(int, sys.stdin.readline().split()))
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# (x,y)기준으로 오른쪽 아래부분의 쓰레기를 치울 수 있음
# y번째 행중 x이후에 쓰레기가 있는지 탐색하고 쓰레기가 있으면 그위치로 이동, 위치값을 0으로 변경
# 재귀로 함수 반복
def cnt(y, x, c):
    bf1 = False
    for j in range(y, n):
        for i in range(x, m):
            if board[j][i] == 1:
                board[j][i] = 0
                c = c + 1 + cnt(j, i, c)
                bf1 = True
            if bf1:
                break
        if bf1:
            break
    return c
# 필요한 로봇의 수는 max(n,m) 이하
v = 1
for i in range(n + 2):
    if v == 0:
        print(i - 1)
        break
    v = cnt(i, 0, 0)