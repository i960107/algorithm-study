from typing import List
from collections import defaultdict
import heapq


def solution(n: int, start: int, end: int, roads: List[List[int]], traps: List[int]) -> int:
    traps = set(traps)
    adj_out = defaultdict(list)
    adj_in = defaultdict(list)

    for u, v, w in roads:
        adj_out[u].append((v, w))
        adj_in[v].append((u, w))

    # end 노드까지의 최단 거리를 구하기 위해서 다른 노드들 까지의 최단 거리를 기록해야하나?
    # 그렇지 않으면 계속 큐에 추가됨?
    INF = int(1e9)
    # distance = [INF] * (n + 1)

    queue = []
    queue.append((0, start, set()))

    while queue:
        dist, now, trapped = heapq.heappop(queue)

        if now == end:
            return dist

        # if distance[now] < dist:
        #     continue

        if now in trapped:
            nxts = adj_in[now]

        else:
            nxts = adj_out[now]

        for nxt, cost in nxts:

            nxt_dist = dist + cost

            # 이미 갔던 곳도 배제할 수 없음...
            # if distance[nxt] <= nxt_dist:
            #     continue

            nxt_trapped = trapped.copy()
            if nxt in traps:
                if nxt in nxt_trapped:
                    nxt_trapped.remove(nxt)
                else:
                    nxt_trapped.add(nxt)

            heapq.heappush(queue, (nxt_dist, nxt, nxt_trapped))


# print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1]], [2, 3]))
