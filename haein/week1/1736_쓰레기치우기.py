# 참고 풀이
# https://dong-gas.tistory.com/22
import sys

n, m = map(int, sys.stdin.readline().split())
room = []
trash = 0
answer = 0
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    room.append(tmp)
    trash += sum(tmp)

def clean(x, y):
    # 함수 안에서 전역변수로 명시해주어야 함 (안 그러면 지역변수로 처리됨)
    global trash
    if x == n-1 and y == m-1:
        if room[x][y] == 1:
            room[x][y] = 0
            trash -= 1
        return
    for i in range(x, n):
        for j in range(y, m):
            if room[i][j] == 1:
                room[i][j] = 0
                trash -= 1
                clean(i, j)
                # 종료 조건 이후 계속 for문을 실행하면 안되고 종료되어야 함 (이미 끝에 도달한 것)
                # 재귀 호출하고 종료조건 만나서 끝났을 때 호출한 쪽에서 더 for문 돌 필요 없으므로 여기에 return
                return

while trash > 0:
    answer += 1
    clean(0, 0)

print(answer)
