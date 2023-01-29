# 참고 풀이
# https://dong-gas.tistory.com/22
n, m = map(int, input().split())
room = [[int(x) for x in input().split()] for _ in range(n)]
trash = sum(sum(r) for r in room)
ans = 0

def clean(x, y):
    # 함수 안에서 전역변수로 명시해주어야 함 (안 그러면 지역변수로 처리됨)
    global trash
    # 종료조건 (끝까지 갔을 때)
    if x == n - 1 and y == m - 1:
        if room[x][y] == 1:
            trash -= 1
            room[x][y] = 0
        return
    for i in range(x, n): # 행
        for j in range(y, m): # 열
            if room[i][j] == 1:
                room[i][j] = 0
                trash -= 1
                clean(i, j)
                return # 종료 조건 이후 계속 for문을 실행하면 안되고 종료되어야 함 (이미 끝에 도달한 것)

while trash > 0:
    ans += 1
    clean(0, 0)
print(ans)
