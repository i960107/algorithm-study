from typing import List


def solution(m: int, n: int, puddles: List[List[int]]) -> int:
    dp = [[0] * m for _ in range(n)]
    # passable 따로 안 두고, dp -1두고, -1이라면 0으로 바꿔줄 수도 있음! 메모리따로 필요 없음.
    passable = [[True] * m for _ in range(n)]
    for x, y in puddles:
        passable[y - 1][x - 1] = False

    for c in range(m):
        if not passable[0][c]:
            break
        dp[0][c] = 1

    for r in range(n):
        if not passable[r][0]:
            break
        dp[r][0] = 1

    for r in range(1, n):
        for c in range(1, m):
            if not passable[r][c]:
                dp[r][c] = 0
                continue
            # 경로 수 자체는 나머지로 기록하기
            dp[r][c] = (dp[r - 1][c] + dp[r][c - 1]) % 1000000007
    return dp[n - 1][m - 1] % 1000000007


# 물에 잠긴 지역은 최대 10개 이므로 리스트 선형 탐색 괜찮음?
# 매번 건널때마다 10번씩 탐색해야하는 것은 비효율적
# 미리 배열 만들어두기
# 주의! puddles는 1부터 시작하는 좌표를 나타냄
# def is_sunk(r: int, c: int, puddles: List[List[int]]) -> bool:
#     for x, y in puddles:
#         if x == c + 1 and y == r + 1:
#             return True
#     return False


print(solution(4, 3, [[2, 2]]))
