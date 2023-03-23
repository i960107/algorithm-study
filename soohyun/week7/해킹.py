from sys import stdin
from typing import List, Dict
from collections import defaultdict
import heapq


# 왜 다익스트라..? 그냥 DFS나 BFS하면 안되나?
# 다익스트라 결과(각 노드들과의 최소거리 중 최대)
# 그냥 BFS인 경우 가중치 처리하기 어려움. 컴퓨터가 감염되기까지의 최단시간을 기록해야함.
def solution(n: int, d: int, c: int, adj: Dict[int, List[int]]) -> List[int]:
    INF = 10000 * 1000 + 1
    queue = [(0, c)]
    distances = [INF] * (n + 1)
    distances[c] = 0

    while queue:
        time, now = heapq.heappop(queue)
        if distances[now] < time:
            continue
        for nxt, s in adj[now]:
            nxt_cost = time + s
            if distances[nxt] <= nxt_cost:
                continue
            distances[nxt] = nxt_cost
            heapq.heappush(queue, (nxt_cost, nxt))

    infection_time = 0
    infected = 0
    for distance in distances:
        if distance == INF:
            continue
        if infection_time < distance:
            infection_time = distance
        infected += 1
    return [infected, infection_time]


read = stdin.readline
t = int(input())
for _ in range(t):
    n, d, c = map(int, read().split())
    adj = defaultdict(list)
    for _ in range(d):
        a, b, s = map(int, read().split())
        adj[b].append((a, s))
    result = solution(n, d, c, adj)
    print(*result)
