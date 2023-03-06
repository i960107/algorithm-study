import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start: int):
    # ELogE
    q = []
    q.append((0, start))

    while q:
        # 큐에서 꺼냈을때 값을 갱신해주면 매번 최단 거리 아닌가?
        acc_dist, curr = heapq.heappop(q)
        if distance[curr] != INF:
            continue
        distance[curr] = acc_dist

        for next, dist in graph[curr]:
            cost = acc_dist + dist
            heapq.heappush(q, (cost, next))


def dijkstra2(start: int):
    # 큐에 최단 경로일때만 넣어주기?
    # 큐에 넣어주면서 값 갱신
    # ELogV. 더 빠름
    q = []
    q.append((0, start))
    distance[start] = 0

    while q:
        # 큐에서 꺼냈을때 값을 갱신해주면 매번 최단 거리 아닌가?
        acc_dist, curr = heapq.heappop(q)
        if distance[curr] < acc_dist:
            continue

        for next, dist in graph[curr]:
            cost = acc_dist + dist
            # 같은 노드가 큐에 두번 이상 삽입되는 경우는 없나?
            # 있음. 더 짧은 경로가 뒤에 등장한 경우. 더 긴 경로는 queue에서 삭제되고 난 후에 무시됨.
            if cost >= distance[cost]:
                continue
            heapq.heappush(q, (cost, next))
            distance[next] = cost


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
