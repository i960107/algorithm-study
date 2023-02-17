from collections import deque, defaultdict

n = int(input())
road = [[0 for _ in range(n)] for _ in range(n)]
k = int(input())
apples = [list(map(int, input().split())) for _ in range(k)]
for x, y in apples:
    road[x][y] = 1
l = int(input())
directions = defaultdict(str)
for i in range(l):
    sec, d = input().split()
    directions[sec] = d
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

time = 0
body = deque([[0, 0]])
move_ind = 0  # 현재 움직이는 방향
cur_x, cur_y = 0, 0  # 현재 좌표


while True:
    time += 1

    cur_x += move[move_ind][0]
    cur_y += move[move_ind][1]

    if str(time) in directions.keys(): # 원래 방향대로 움직이면 됨
        if directions[str(time)] == 'D':
            move_ind = (move_ind + 1) % 4
        else:
            if move_ind == 0:
                move_ind = 3
            else:
                move_ind -=1

    if cur_x < 0 or cur_x >= n or cur_y < 0 or cur_y >= n: # 이동한 곳이 벽일 때
        break
    elif road[cur_x][cur_y] in body: # 이동한 곳이 몸일 때
        break
    elif road[cur_x][cur_y] == 1: # 이동한 곳이 사과일 때
        road[cur_x][cur_y] = 0
        body.append([cur_x, cur_y])
    else: # 이동할 수 있는 곳일 때
        body.append([cur_x, cur_y])
        body.popleft()

answer = time
print(answer)

'''
0 : 갈 수 있는 곳
1 : 사과 있는 곳
머리 이동 -> (+1) -> 해당 좌표가 벽 or 몸 -> 종료
                                    -> 아니라면 사과 유무 확인 -> 사과 없으면 deque에서 popleft() 
                                                        -> 사과 있으면 deque에 현재 좌표(머리) append() 
이동한 곳이 사과이고 몸일때..?
'''
