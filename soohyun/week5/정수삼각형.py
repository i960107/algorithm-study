from typing import List


# 높이가 h일때 O(h^2) -> 500 * 500  괜찮음
def solution(triangle: List[List[int]]) -> int:
    h = len(triangle)

    for r in range(h - 2, -1, -1):
        for c in range(len(triangle[r])):
            triangle[r][c] += max(triangle[r + 1][c], triangle[r + 1][c + 1])
    return triangle[0][0]


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
