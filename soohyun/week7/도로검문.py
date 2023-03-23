import sys
from sys import stdin, maxsize
from collections import defaultdict
import heapq


# 시간 초과.. 5000 * (1000 Log 5000) = 65,000,000
# => 최단 경로에 포함된든 간선을 block하는 경우만 세기.
def get_max_time_with_check(start: int, end: int) -> int:
    distances = [[INF, i] for i in range(N + 1)]
    queue = [(0, 1)]
    distances[1][0] = 0

    while queue:
        now_dist, now = heapq.heappop(queue)
        if distances[now][0] < now_dist:
            continue
        for nxt, cost in adj[now]:
            nxt_dist = now_dist + cost
            if (now, nxt) == (start, end) or (now, nxt) == (end, start):
                continue
            if distances[nxt][0] <= nxt_dist:
                continue
            distances[nxt][0] = nxt_dist
            distances[nxt][1] = now
            heapq.heappush(queue, (nxt_dist, nxt))

    # 최단 경로에서 거치는 간선 추가
    if (start == end == 0):
        global blocks
        now = N
        while True:
            if now == 1:
                break
            nxt = distances[now][1]
            blocks.append((now, nxt))
            now = nxt

    return distances[N][0]


INF = sys.maxsize
read = stdin.readline
N, M = map(int, input().split())
adj = defaultdict(list)
# 검문 없을때 지연 시간
blocks = []
for _ in range(M):
    a, b, t = map(int, read().split())
    adj[a].append((b, t))
    adj[b].append((a, t))

distance_without_block = get_max_time_with_check(0, 0)
distance = distance_without_block
# 탈출 최대 지연 시간.
# 노드가 아닌 간선을 막는 것!
# 양방향 간선으로, 더블 체크하면 안됨.

for start, end in blocks:
    result = get_max_time_with_check(start, end)
    if distance < result:
        distance = result
# 지연 효과가 없을때 -> block없을때랑 탈출 시간이 똑같을때?
if distance <= distance_without_block:
    print("0")
elif distance == INF:
    print("-1")
else:
    print(distance - distance_without_block)
