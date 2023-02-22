from typing import List


# 안전한 영역의 최대 개수
# 최대로 나누어지는 영역의 개수
# 비가 더 내린면 안전한 영역의 개수가 줄어들 수도, 늘어날수도.
# 전체 탐색을 해봐야함? 10,000 * 100번
def solution(n: int, heights: List[List[int]]) -> int:
    rain = 0
    max_safety_areas = 0
    while True:
        safety_area = get_safety_areas(n, heights, rain)
        if safety_area == 0:
            break
        max_safety_areas = max(safety_area, max_safety_areas)
        rain += 1
    return max_safety_areas


# 비가 rain 만큼 내렸을때 안전 영역의 수를 구하는 함수
def get_safety_areas(n: int, heights: List[List[int]], rain: int) -> int:
    visited = [[False] * n for _ in range(n)]
    count = 0
    for r in range(n):
        for c in range(n):
            if visited[r][c]:
                continue
            if heights[r][c] <= rain:
                continue
            count += 1
            dfs(n, r, c, heights, visited, rain)
    return count


# 매개변수가 너무 많음.. 실무에서라면 어떻게 줄였을까?
# r,c가 포함된 안전 영역을 dfs로 탐색
def dfs(n: int, r: int, c: int, heights: List[List[int]], visited: List[List[bool]], rain: int):
    # 상, 하, 좌, 우
    dr = (0, 0, -1, 1)
    dc = (-1, +1, 0, 0)

    stack = [(r, c)]
    while stack:
        curr_r, curr_c = stack.pop()
        if not (0 <= curr_r < n and 0 <= curr_c < n) or visited[curr_r][curr_c]:
            continue
        visited[curr_r][curr_c] = True

        if heights[curr_r][curr_c] <= rain:
            continue

        for k in range(4):
            next_r, next_c = curr_r + dr[k], curr_c + dc[k]
            stack.append((next_r, next_c))


n = int(input())
heights = []
for _ in range(n):
    heights.append(list(map(int, input().split())))

print(solution(n, heights))
