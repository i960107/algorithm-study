import copy
from typing import List


# 시간 복잡도를 낮추는 방법?
def solution_brute_force(board: List[List[int]], skill: List[List[int]]) -> int:
    N, M = len(board), len(board[0])
    ATTACK, DEFNSE = 1, 2

    for type, r1, c1, r2, c2, degree in skill:
        if type == ATTACK:
            degree *= -1
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                board[r][c] += degree

    count = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] > 0:
                count += 1
    return count


# 시간 복잡도 그다지 줄여지지 않음.
# union -find도 시간 복잡도 안 줄여질 거 같은데..
def solution_only_destroyed_buildings(board: List[List[int]], skill: List[List[int]]) -> int:
    N, M = len(board), len(board[0])
    ATTACK, DEFNSE = 1, 2

    attacks = []
    defenses = []
    for type, *args in skill:
        if type == ATTACK:
            attacks.append(args)
        else:
            defenses.append(args)

    destroyed = set()
    for r1, c1, r2, c2, degree in attacks:
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                board[r][c] -= degree
                if board[r][c] <= 0:
                    destroyed.add((r, c))

    final_destroyed = copy.deepcopy(destroyed)
    for r, c in destroyed:
        for r1, c1, r2, c2, degree in defenses:
            if r1 <= r <= r2 and c1 <= c <= c2:
                board[r][c] += degree
                if board[r][c] > 0:
                    final_destroyed.remove((r, c))
                    break
    return N * M - len(final_destroyed)


# prefix sum 구하기
# 값이 변화하는 지점에 기록하는 것 vs 누적합 차이?
def solution(board: List[List[int]], skill: List[List[int]]) -> int:
    n, m = len(board), len(board[0])
    ATTACK, DEFENSE = 1, 2

    affected = [[0] * m for _ in range(n)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == ATTACK:
            affected[r1][c1] -= degree
            if r2 + 1 < n:
                affected[r2 + 1][c1] += degree
            if c2 + 1 < m:
                affected[r1][c2 + 1] += degree
            if r2 + 1 < n and c2 + 1 < m:
                affected[r2 + 1][c2 + 1] -= degree

        else:
            affected[r1][c1] += degree
            if r2 + 1 < n:
                affected[r2 + 1][c1] -= degree
            if c2 + 1 < m:
                affected[r1][c2 + 1] -= degree
            if r2 + 1 < n and c2 + 1 < m:
                affected[r2 + 1][c2 + 1] += degree

    for r in range(n):
        for c in range(m):
            if r - 1 >= 0:
                affected[r][c] += affected[r - 1][c]
            if c - 1 >= 0:
                affected[r][c] += affected[r][c - 1]
            if r - 1 >= 0 and c - 1 >= 0:
                affected[r][c] -= affected[r - 1][c - 1]

    count = 0
    for r in range(n):
        for c in range(m):
            board[r][c] += affected[r][c]
            if board[r][c] > 0:
                count += 1

    # affected누적합 안 구해진 상태로 바로 더하면 틀림
    # for r in range(n):
    #     for c in range(m):
    #         board[r][c] += affected[r][c]
    #         if r - 1 >= 0:
    #             board[r][c] += affected[r - 1][c]
    #         if c - 1 >= 0:
    #             board[r][c] += affected[r][c - 1]
    #         if r - 1 >= 0 and c - 1 >= 0:
    #             board[r][c] -= affected[r - 1][c - 1]
    #         if board[r][c] > 0:
    #             count += 1

    return count


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
