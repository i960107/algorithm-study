import sys
from heapq import heappush, heappop

# 풀이 2 (56ms)
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())

# graph[a] = (b, cost) : a -> b
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start, graph):
    q = []
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heappop(q)

        if distance[now] < dist:
            continue

        for b, cost in graph[now]:
            cost = dist + cost
            if cost < distance[b]:
                distance[b] = cost
                heappush(q, (cost, b))

dijkstra(x, graph)
result = [0 for _ in range(n+1)]
for i in range(1, n+1):
    result[i] = distance[i]

distance = [INF] * (n+1)
opp_graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    for b, c in graph[i]:
        opp_graph[b].append((i, c))
dijkstra(x, opp_graph)

for i in range(1, n+1):
    result[i] += distance[i]

print(max(result))



'''
- 정점 -> 2
- 2 -> 정점

다익스트라 
A로부터 모든 정점까지의 최단 거리 (A로부터 시작해서 각 점까지의 최단 거리)
즉, 특정 한 점에서 출발하는 최단 경로를 싹 다 구해줌!

고민 
정점 -> 2까지 가는 방식을 어떻게 구해야 할 것인가?
O(ElogV) -> 1000 * 100 = 100000
여기에 각 점별로 만약 한다면 100000000 : 시간 복잡도가 1억이 나와서 잘 되지 않을 것 같음.. 

문제
O(ElogV) 시간이 걸리는 건 정상인데, 그걸 N번이나 돌리고 있다는 게 문제
특정 한 점에서 출발하는 최단 경로를 싹 다 구해준다는 사실을 활용하여 간선 방향을 다 반대로 뒤집은 다음, 파티장에서 다익스트라를 1번만 돌리면 됨
2번에서 출발해서 각 정점으로의 최단 거리 but, 거꾸로 가는 것이므로 모든 간선의 방향을 반대로 뒤집기
'''

'''
첫 번째 풀이 (940ms)
모든 점에 대하여 다익스트라 수행
import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())

# graph[a] = (b, cost) : a -> b
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heappop(q)

        if distance[now] < dist:
            continue

        for b, cost in graph[now]:
            cost = dist + cost
            if cost < distance[b]:
                distance[b] = cost
                heappush(q, (cost, b))

dijkstra(x)
result = [0 for _ in range(n+1)]
for i in range(1, n+1):
    result[i] = distance[i]

for i in range(1, n+1):
    distance = [INF] * (n+1)
    if i == x:
        continue
    else:
        dijkstra(i)
        result[i] += distance[x]

print(max(result)) 

'''
