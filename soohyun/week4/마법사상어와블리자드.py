from typing import List


# 1번째 칸부터 오른쪽, 아래, 왼쪽, 위, n-1번씩 4번, n-2번씩 4번, 2번씩 4번

def solution(n: int, grid: List[List[int]], magics: List[List[int]]) -> List[int]:
    answer = [0] * 3
    for d, s in magics:
        do_the_magic(d, s, grid)


# 처음에는 폭발할 구슬이 없는 상태인가?
# 마법과 폭발을 한번에 처리할 수 있나?. 250개의 칸을 매번 탐색?
def do_the_magic(n: int, d: int, s: int, grid: List[List[int]]) -> List[int]:
    # 블리자드 마법을 부리고
    # 폭발하는 구슬이 없을때까지
    # 구슬이 폭발하고
    # 구슬이 이동
    shark = (n // 2, n // 2)
    # 위, 아래, 왼쪽, 오른쪽
    magic_direction = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))

    for distance in range(s):
        grid[shark[0] + magic_direction[d][0]][shark[1] + magic_direction[d][1]] = 0

    dr = (0, 1, 0, -1)
    dc = (1, 0, -1, 0)
    r, c = 0, 0
    # 구슬이 이동
    # 어떻게 이동하는게 좋은방법일까?
    # 삼중 for문 보다 더 나은 방법이 있을까?
    for cnt in range(n - 1, 1, -1):
        k = 0
        while k < 4:
            for _ in range(cnt):
                nr, nc = r + dr[k], c + dc[k]
            k += 1

    for cnt in range(n - 1, 1, -1):
        k = 0
        while k < 4:
            for _ in range(cnt):
                nr, nc = r + dr[k], c + dc[k]
            k += 1


def marble_changes(grid: List[List[int]]) -> List[int]:
    pass


n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

magics = []
for _ in range(m):
    magics.append(list(map(int, input().split())))

print([index * value for index, value in enumerate(solution(n, grid, magics), 1)])
