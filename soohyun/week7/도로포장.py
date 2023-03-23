import copy
import sys
from sys import stdin
from collections import defaultdict
import heapq

read = stdin.readline
sys.setrecursionlimit(10 ** 6)
N, M, K = map(int, input().split())
adj = defaultdict(list)
# 10,000 C 20다  고려할 수 없음!

for _ in range(M):
    a, b, t = map(int, read().split())
    adj[a].append((b, t))
    adj[b].append((a, t))

'''풀이1 실패-다익스트라(문제 조건 만족 못함)'''
# # 1에서 N까지 최단시간.
# # 1에서 N까지 가는 최단시간 경로의 cost들을 기록한다
# INF = int(1e9)
# # 최단 거리, 이전 노드
# shortest_path = [[INF, i] for i in range(N + 1)]
# queue = []
# queue.append((0, 1))
# shortest_path[1][0] = 0
#
# # 다익스트라
# # 최소 경로를 알아야하는데...
# while queue:
#     dist, now = heapq.heappop(queue)
#     if shortest_path[now][0] < dist:
#         continue
#     for nxt, cost in adj[now]:
#         if shortest_path[nxt][0] <= dist + cost:
#             continue
#         shortest_path[nxt] = [dist + cost, now]
#         heapq.heappush(queue, (dist + cost, nxt))
#
# # K번째 수를 뺀다
# # N이 가장 멀까..?
# costs = []
# now = N
# while now != 1:
#     cost, nxt = shortest_path[now]
#     heapq.heappush(costs, cost)
#     now = nxt
#
# # 최단 거리아닌 경우가 정답일 수도 있는데... -> 모든 경로를 살펴봐야함.
# total_cost_after_pavement = 0
# for _ in range(0, len(costs) - K):
#     if not costs:
#         break
#     cost = heapq.heappop(costs)
#     total_cost_after_pavement += cost
#
# print(total_cost_after_pavement)
#

# 1 -> N까지의 모드 경로를 살펴보고 싶음

'''풀이2 실패-dfs 모든 경로 탐색(시간초과)`'''
# def dfs(now: int, cost: int, costs: List[int], visited: List[bool]):
#     visited[now] = True
#     costs.append(cost)
#
#     if now == N:
#         cost_after_pavement = get_cost_after_pavement(copy.deepcopy(costs), N, K)
#         global answer
#         if cost_after_pavement < answer:
#             answer = cost_after_pavement
#     else:
#         for nxt, nxt_cost in adj[now]:
#             if visited[nxt]:
#                 continue
#             dfs(nxt, nxt_cost, costs, visited)
#
#     visited[now] = False
#     costs.pop()
#
#
# def get_cost_after_pavement(costs: List[int], N: int, K: int) -> int:
#     total_cost_after_pavement = 0
#     for _ in range(0, len(costs) - K):
#         if not costs:
#             break
#         cost = heapq.heappop(costs)
#         total_cost_after_pavement += cost
#     return total_cost_after_pavement
#
#
# start = 1
# path = []
# visited = [False] * (N + 1)
# visited[start] = True
# answer = int(1e9)
# dfs(start, 0, path, visited)
# print(answer)


'''풀이3-2차원 다익스트라'''
INF = float('INF')

# 2차원 다익스트라 배열. 현재 정점 i에서 포장을 j개 했을때 드는 최소거리
distance = [[INF] * (K + 1) for _ in range(N + 1)]
queue = []
for k in range(1, K + 1):
    distance[1][k] = 0
# 거리, 노드번호, 포장된 도로 개수
heapq.heappush(queue, (0, 1, 0))

# 필요 없나..?
# for i in range(1, N + 1):
#     for k in range(1, K + 1):
#         distance[i][k] = 0


while queue:
    now_dist, now, paved = heapq.heappop(queue)
    if distance[now][paved] < now_dist:
        continue

    # 현재 정점에서 포장이 가능한 경우
    if paved + 1 <= K:
        for nxt, cost in adj[now]:
            if distance[nxt][paved + 1] <= now_dist:
                continue
            distance[nxt][paved + 1] = now_dist
            heapq.heappush(queue, (now_dist, nxt, paved + 1))

    for nxt, cost in adj[now]:
        nxt_dist = now_dist + cost
        if distance[nxt][paved] <= nxt_dist:
            continue
        distance[nxt][paved] = nxt_dist
        heapq.heappush(queue, (nxt_dist, nxt, paved))

for row in distance:
    print(row)
ans = INF
for p in range(K + 1):
    if distance[N][p] < ans:
        ans = distance[N][p]
print(ans)
