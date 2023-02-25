from typing import List, Tuple
from itertools import groupby

N, M = map(int, input().split())
beads = []
for _ in range(N):
    beads.append(list(map(int, input().split())))
magics = []
for _ in range(M):
    magics.append(list(map(int, input().split())))

# popped[i] = 폭발한 i번 구슬의 개수
popped = [] * 4


def make_coord() -> List[Tuple[int, int]]:
    coord = []
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    d = -1
    r, c = N // 2, N // 2
    # 어떻게 삼중 for문을 빠져나오지 -> 바로 return시키지
    for count in range(1, N + 1):
        for _ in range(2):
            d = (d + 1) % 4
            for _ in range(count):
                r += directions[d][0]
                c += directions[d][1]
                coord.append((r, c))
                if len(coord) == (N * N) - 1:
                    return coord

    # for count in range(1, N):
    #     for _ in range(2):
    #         d = (d + 1) % 4
    #         for _ in range(count):
    #             r += directions[d][0]
    #             c += directions[d][1]
    #             coord.append((r, c))
    #         if len(coord) == N * N - 1:
    #             break


def make_coord_reverse() -> List[Tuple[int, int]]:
    coord = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = -1
    r, c = 0, 0

    # count를 어디서부터 시작할지가 애매함...
    # count아닌 다른 방식을 쓰는게 좋을 듯
    def is_valid_coord(r: int, c: int) -> bool:
        if 0 <= r < N and 0 <= c < N:
            return True
        return False

    visited = [[False] * N for _ in range(N)]
    visited[r][c] = True
    coord.append((r, c))

    while len(coord) < (N * N) - 1:

        nr, nc = r + directions[d][0], c + directions[d][1]
        if not is_valid_coord(nr, nc) or visited[nr][nc]:
            d = (d + 1) % 4
            continue

        visited[r][c] = True
        coord.append((nr, nc))
        r, c = nr, nc

    return coord


# coord = make_coord()
board = [[0] * N for _ in range(N)]
# sequence = 1
# for r, c in coord:
#     board[r][c] = sequence
#     sequence += 1
#
# for row in board:
#     print(row)

# coord = make_coord_reverse()
# sequence = 1
# for r, c in coord:
#     board[r][c] = sequence
#     sequence += 1
# for row in board:
#     print(row)

shark = (N // 2, N // 2)
coord = make_coord()

for d, s in magics:
    directions = [(0, 0), (-1, 0), (1, 0), (-1, 0), (0, 1)]
    for distance in range(1, s + 1):
        beads[shark[0] + directions[d][0] * distance][shark[1] + directions[d][1] * distance] = 0


def pop_and_move():
    numbers = []
    for r, c in coord:
        if beads[r][c] != 0:
            numbers.append(beads[r][c])

    groups = groupby(numbers)
    for num, group in groups:
        if len(group) >= 4:
            popped[num] += len(group)
            continue



while True:
    popped = 0

    if popped == 0:
        break

move()
# for row in beads:
#     print(row)
