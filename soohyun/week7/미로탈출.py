from typing import List

import heapq
from collections import defaultdict


def solution(n: int, start: int, end: int, roads: List[List[int]], traps: List[int]) -> int:
    INF = int(1e9)

    # in, out 버전 따로 기록해야하나
    original = defaultdict(list)
    alternative = defaultdict(list)
    for u, v, c in roads:
        original[u].append((v, c))
        alternative[v].append((u, c))

    traps = set(traps)

    # untrapped, trapped
    distance = [[INF, INF] for _ in range(n + 1)]
    queue = []
    # distance, node, is_trapped
    queue.append((0, start, 0))
    distance[start][0] = 0

    while queue:
        now_dist, now, is_trapped = heapq.heappop(queue)
        if distance[now_dist][now] < is_trapped:
            continue
        for nxt, cost in in_adj[now]:
            nxt_dist = now_dist + cost


print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
