from typing import List
from collections import defaultdict
import heapq


def solution(n: int, start: int, end: int, roads: List[List[int]], traps: List[int]) -> int:
    INF = int(1e9)
    T = len(traps)

    adj = defaultdict(list)
    for u, v, w in roads:
        adj[u].append((v, w, False))
        adj[v].append((u, w, True))

    distance = [[INF] * (1 << T) for _ in range(n + 1)]
    distance[start][0] = 0

    # 노드번호: id
    trap_ids = dict()
    for index, trap in enumerate(traps):
        trap_ids[trap] = index

    queue = [(0, start, 0b0)]

    while queue:
        dist, now, trapped = heapq.heappop(queue)

        if distance[now][trapped] < dist:
            continue

        is_now_trapped = (now in trap_ids and (trapped & (1 << trap_ids[now])))

        # trap on/off = bitmask ^ (1<<trap_id)
        # is_trap_on = bitmaks & (1<<trap_id)
        for nxt, cost, is_reversed in adj[now]:
            is_nxt_trapped = (nxt in trap_ids and (trapped & (1 << trap_ids[nxt])))
            nxt_trapped = trapped
            if nxt in trap_ids:
                nxt_trapped = trapped ^ (1 << trap_ids[nxt])
            nxt_dist = dist + cost
            if (is_now_trapped and is_nxt_trapped) or (not is_now_trapped and not is_nxt_trapped):
                if is_reversed:
                    continue
            else:
                if not is_reversed:
                    continue
            if distance[nxt][nxt_trapped] <= nxt_dist:
                continue
            distance[nxt][nxt_trapped] = nxt_dist
            heapq.heappush(queue, (nxt_dist, nxt, nxt_trapped))

    min_distance = INF

    for dist in distance[end]:
        if dist < min_distance:
            min_distance = dist

    return min_distance
