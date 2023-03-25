import heapq
import sys
from collections import defaultdict
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(s, grp, inject):
    q = []
    heapq.heappush(q, (0, s))
    distance = [sys.maxsize] * (n+1)
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        # print(dist, now, distance[now], inject[now])

        for d, c in grp[now]:
            cost = dist + c
            # print(now, d, c, distance, distance[d], inject, inject[d], cost)
            if cost < distance[d]:
                distance[d] = cost
                inject[d] = 1
                heapq.heappush(q, (cost, d))
                # print(d, '바뀜')
            # print(now, d, c, distance)

    cnt, time = 0, 0
    for k in inject.keys():
        if inject[k] == 1:
            cnt += 1

    # print('거리', distance)

    if max(distance) == INF:
        for d in range(len(distance)):
            if distance[d] == INF:
                distance[d] = 0
    time = max(distance)

    return (cnt, time)


t = int(input())

for i in range(t):
    n, d, start = map(int, input().split())
    graph = [[] for k in range(n+1)]
    inject = defaultdict(int)
    for i in range(n):
        inject[i+1] = 0
    inject[start] = 1 # 1인 점은 감염됨

    for j in range(d):
        a, b, c = map(int, input().split())
        graph[b].append((a, c)) # b -> a 비용 c

    cnt, time = dijkstra(start, graph, inject)

    print(cnt, time)


