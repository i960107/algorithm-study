import sys
from collections import defaultdict
from sys import stdin, maxsize
import heapq

read = stdin.readline
# 최단 거리... 0에서 n-1로 가는 최단 거리.
N, M = map(int, input().split())

# string 바로 bool로 변환 안됨
# visible = list(map(bool, read().split()))
visible = list(map(int, read().split()))
visible[-1] = 0

adj = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, read().split())
    adj[a].append((b, t))
    adj[b].append((a, t))

# int(1e9) 하면 에러남.. 1e9
INF = sys.maxsize
distances = [INF] * N

queue = []
heapq.heappush(queue, (0, 0))
distances[0] = 0

# 시간 초과 왜? -> 입력시 readline으로 읽기!
while queue:
    dist, now = heapq.heappop(queue)

    # 등호 포함하면 안됨.
    # 최단 경로일때만 처리하기
    if distances[now] < dist:
        continue

    for nxt, next_cost in adj[now]:
        cost = dist + next_cost

        # 등호 포함.
        # 인접 노드를 큐에 추가할때 cost가 같은 경우에도 추가해야하는 것 아닌가? cost가 같아도 다른 경로일 수 있지 않나?
        # 최단 거리인 경우에만 큐에 추가해주기
        # if distances[next] <= next_cost:
        #     continue
        #
        # if visible[next]:
        #     continue
        #

        if cost < distances[nxt] and visible[nxt] == 0:
            distances[nxt] = cost
            heapq.heappush(queue, (cost, nxt))

print(distances[- 1] if distances[- 1] < INF else -1)

print(int(1e9))
print(sys.maxsize)
print(float('inf'))
