import sys
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def make_one_list():
    cur_x = (N // 2) + 1
    cur_y = (N // 2) + 1
    # 2,2 -> 3,3 -> 4,4 ...방식으로 변이 나열
    move_num = 2
    while cur_y > 0:
        for i in range(1, 5):
            for j in range(move_num):
                if i == 1 and j == 0:
                    cur_y -= 1
                else:
                    cur_x += dx[i]
                    cur_y += dy[i]
                one_list.append()