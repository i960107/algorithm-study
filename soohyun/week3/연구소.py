from typing import List, Tuple
from itertools import combinations
from collections import deque


def solution(n: int, m: int, graph: List[List[int]]) -> int:
    empty = []
    virus = []
    for r in range(n):
        for c in range(m):
            if graph[r][c] == 2:
                virus.append((r, c))
            elif graph[r][c] == 0:
                empty.append((r, c))

    # 빈칸 중 세 칸을 선택
    max_safety_area = 0
    print(len(list(combinations(range(len(empty)),3))))
    for combi in combinations(range(len(empty)), 3):
        temp_graph = graph.copy()
        for x in combi:
            r, c = empty[x][0], empty[x][1]
            temp_graph[r][c] = 1
        spread_virus(virus, temp_graph)
        safety_area = get_safety_area(n, m, temp_graph)
        max_safety_area = max(max_safety_area, safety_area)

    return max_safety_area


# Tuple은 immutable 타입이기 때문에 int개수만큼 써주어야, 요소 개수 유연하게 하려면 Tuple[int, ...]
def spread_virus(virus: [List[int]], graph: List[List[int]]):
    for r, c in virus:
        dfs(r, c, graph)


def get_safety_area(n: int, m: int, graph: List[List[int]]) -> int:
    count = 0
    for r in range(n):
        for c in range(m):
            if graph[r][c] != 0:
                continue
            count += 1
            bfs(r, c, graph)
        return count


def bfs(r: int, c: int, graph: List[List[int]]):
    queue = deque()
    queue.append((r, c))

    while queue:
        cr, cc = queue.popleft()
        if graph[cr][cc] != 0:
            continue
        graph[cr][cc] = 3
        dr = (-1, 1, 0, 0)
        dc = (0, 0, -1, 1)

        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]):
                queue.append((nr, nc))


# visited 를 따로 관리해주어야하는데.
def dfs(r: int, c: int, graph: List[List[int]]):
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    stack = [[r, c]]
    while stack:
        cr, cc = stack.pop()
        if graph[cr][cc] == 1:
            continue
        graph[cr][cc] = 2
        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]):
                stack.append((nr, nc))


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
print(solution(n, m, graph))
