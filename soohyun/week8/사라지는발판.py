from typing import List


def solution(board: List[List[int]], aloc: List[int], block: List[int]) -> int:
    INF = int(1e9)
    EMPTY = 0
    N, M = len(board), len(board[0])

    dr = (0, 0, 1, -1)
    dc = (1, -1, 0, 0)

    def is_valid_coord(r: int, c: int) -> bool:
        if 0 <= r < N and 0 <= c < M:
            return True
        return False

    def is_finished(r: int, c: int):
        # 상,하,좌,우 한 군데라도 발판이 있다면 이동가능
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if not is_valid_coord(nr, nc):
                continue

            if board[nr][nc]:
                return False
        return True

    # player1이 움직임
    def _solution(r1: int, c1: int, r2: int, c2: int) -> List[int]:
        if is_finished(r1, c1):
            # can_win, turn
            return [False, 0]
        if r1 == r2 and c1 == c2:
            return [True, 1]

        max_turn = 0
        min_turn = INF
        can_win = False

        for k in range(4):
            nr = r1 + dr[k]
            nc = c1 + dc[k]

            if not is_valid_coord(nr, nc):
                continue
            if board[nr][nc] == 0:
                continue

            # plyaer1이 r1, c1 -> nr, nc로 이동
            board[r1][c1] = 0
            result = _solution(r2, c2, nr, nc)
            # 재귀 후 값 되돌려주기
            board[r1][c1] = 1

            # result[0]이 False여야 현재 턴에서 내가 이길 수 있음
            if not result[0]:
                can_win = True
                min_turn = min(min_turn, result[1])
            elif not can_win:
                max_turn = max(max_turn, result[1])
        turn = min_turn if can_win else max_turn
        return [can_win, turn + 1]

    return _solution(*aloc, *block)[1]


print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))
