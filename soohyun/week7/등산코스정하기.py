from typing import List
from collections import defaultdict
import heapq


def solution(n: int, paths: List[List[int]], gates: List[int], summits: List[int]) -> List[int]:
    INF = int(1e9)
    summits = set(summits)
    adj = defaultdict(list)
    for i, j, w in paths:
        adj[i].append((j, w))
        adj[j].append((i, w))

    queue = []
    # intensity, node

    distance = defaultdict(lambda: INF)

    for gate in gates:
        # 출발 노드의 distance 초기화해주는 거 잊지말기!
        distance[gate] = 0
        heapq.heappush(queue, (0, gate))

    while queue:
        intensity, now = heapq.heappop(queue)

        if distance[now] < intensity:
            continue

        for nxt, cost in adj[now]:
            if cost < intensity:
                cost = intensity
            # 최단 경로일때만 추가해주기........
            # 안그러면 queue가 안 끝남..
            if distance[nxt] <= cost:
                continue
            distance[nxt] = cost
            if nxt in summits:
                continue
            heapq.heappush(queue, (cost, nxt))

    final_intensity, final_summit = INF, -1

    # set은 순서 없음 주의!
    for summit in summits:
        intensity = distance[summit]
        if intensity < final_intensity or (intensity == final_intensity and summit < final_summit):
            final_intensity, final_summit = intensity, summit
    return [final_summit, final_intensity]


print(
    solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
