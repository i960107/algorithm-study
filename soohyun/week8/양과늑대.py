from typing import List
from collections import defaultdict


def solution(info: List[int], edges: List[List[int]]) -> int:
    SHEEP = 0
    WOLF = 1

    adj = defaultdict(list)

    for u, v in edges:
        adj[u].append(v)

    answer = []

    def dfs(now: int, sheeps: int, wolves: int, nxts: List[int]) -> int:
        if info[now] == SHEEP:
            sheeps += 1
        else:
            wolves += 1
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        sheeps = 0

        for p, c in edges:
            if visited[p] and not visited[c]:
        return sheeps

    visited = [False] * len(info)
    return dfs(0, 0, 0)


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
