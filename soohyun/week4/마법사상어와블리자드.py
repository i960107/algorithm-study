from typing import List
from itertools import groupby, chain


# 1번째 칸부터 오른쪽, 아래, 왼쪽, 위, n-1번씩 4번, n-2번씩 4번, 2번씩 4번

def solution(n: int, beads: List[List[int]], magics: List[List[int]]):
    for d, s in magics:
        do_the_magic(n, d, s, beads)


def do_the_magic(n: int, d: int, s: int, beads: List[List[int]]):
    # 블리자드 마법을 부리고

    shark = (n // 2, n // 2)
    magic_direction = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))

    r, c = n // 2, n // 2
    for distance in range(1, s + 1):
        r += magic_direction[d][0]
        c += magic_direction[d][1]
        beads[r][c] = 0

    # 구슬이 이동, 폭발하고(3개 이상일 경우에만)
    arr = [[] for _ in range(2)]
    b = 0
    global answer
    for r, c in coords:
        if beads[r][c]:
            arr[b].append(beads[r][c])

    while True:
        is_boomed = False

        for bead, gr in groupby(arr[b]):
            tmp = list(gr)
            if len(tmp) >= 4:
                is_boomed = True
                answer += bead * len(tmp)
            else:
                # 폭발하고 남은 것만 저장. arr[0], arr[1]에 번갈아 가몀ㄴ서
                # b 가 0이면 1, 1이면 0
                arr[b ^ 1] += tmp
        arr[b].clear()
        b ^= 1

        if not is_boomed:
            break

    for i in range(N):
        for j in range(N):
            beads[i][j] = 0
    # 구슬 변화
    nxt = chain.from_iterable((len(list(gr)), bead) for bead, gr in groupby(arr[b]))
    for (r, c), val in zip(coords[1:], nxt):
        beads[r][c] = val


def make_coord():
    dr = (0, 1, 0, -1)
    dc = (-1, 0, 1, 0)

    ret = [(N // 2, N // 2)]
    d = 0
    for s in range(1, N + 1):
        for _ in range(2):
            for _ in range(s):
                r, c = ret[-1]
                nr, nc = r + dr[d], c + dc[d]
                ret.append((nr, nc))
                if len(ret) >= N * N:
                    return ret
            d = (d + 1) % 4


# 구슬 파괴(마법)->구슬 이동->구슬 폭발->구슬 변화
N, M = map(int, input().split())
beads = [list(map(int, input().split())) for _ in range(N)]
magics = []
for _ in range(M):
    magics.append(list(map(int, input().split())))

answer = 0
coords = make_coord()
solution(N, beads, magics)

print(answer)
