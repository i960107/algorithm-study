from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N = int(input())
apples = sorted(tuple(map(int, input().split())) for _ in range(int(input())))
mv = [0] * 10001
for _ in range(int(input())):
    X, C = input().split()
    mv[int(X)] = C
snake = deque()
snake.append((1, 1))
d = 0
t = 0


def is_valid_coord(y, x):
    return 1 <= y <= N and 1 <= x <= N


while True:
    t += 1
    y, x = snake[0]
    ny = y + dy[d]
    nx = x + dx[d]
    if is_valid_coord(ny, nx) and (ny, nx) not in snake:
        snake.appendleft((ny, nx))
    else:
        break

    if (ny, nx) in apples:
        apples.remove((ny, nx))
    else:
        snake.pop()

    if mv[t]:
        if mv[t] == "D":
            d = (d + 1) % 2
        else:
            d = (d + 3) % 4
print(t)
# 덱의 앞, 뒤에 뱀의 머리, 꼬리를 저장
