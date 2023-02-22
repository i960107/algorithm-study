import sys
from collections import deque
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
graph = [[0] * n for _ in range(n)]

for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = 2
L = int(sys.stdin.readline())
dic = {}
for _ in range(L):
    t, alpha = map(str, sys.stdin.readline().split())
    dic[int(t)] = alpha
cnt, direction = 0, 0
x, y = 0, 0
graph[x][y] = 1
dq = deque()
dq.append((0,0))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def turn(alpha):
    global direction
    if alpha == 'D':
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4

while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]
    if x < 0 or x >= n or y < 0 or y >= n or (x, y) in dq:
        break
    # 뱀이 이동한 위치에 사과가 있는경우 -> 뱀의 몸길이는 증가
    if graph[x][y] == 2:
        graph[x][y] = 1
        dq.append((x, y))
        if cnt in dic:
            turn(dic[cnt])
    # cnt가 dic에 있는 시간이랑 같을때 -> 방향전환
    elif graph[x][y] == 0:
        graph[x][y] = 1
        dq.append((x, y))
        tx, ty = dq.popleft()
        graph[tx][ty] = 0
        if cnt in dic:
            turn(dic[cnt])
    else:
        break
print(cnt)
