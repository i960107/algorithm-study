from heapq import heappush, heappop
import sys, copy

def solution(n, s, A, B, fares):
    answer = 0
    INF = sys.maxsize
    graph = [[] for i in range(n+1)]
    distance = [INF] * (n+1)

    for a, b, c in fares:
        graph[a].append((b, c))
        graph[b].append((a, c))

    def dijkstra(start, distance):
        q = []
        heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heappop(q)

            if dist > distance[now]:
                continue

            for b, c in graph[now]:
                cost = dist + c
                if distance[b] > cost:
                    distance[b] = cost
                    heappush(q, (cost, b))
        return distance

    # 합승 X
    tmp_distance = dijkstra(s, copy.deepcopy(distance))
    no_result = tmp_distance[A] + tmp_distance[B]


    # 합승 O
    yes_result = []
    for i in range(1, n+1):
        if i == s:
            continue
        tmp_result = tmp_distance[i]
        yes_distance = dijkstra(i, copy.deepcopy(distance))
        yes_result.append(tmp_result + yes_distance[A] + yes_distance[B])

    answer = min(no_result, min(yes_result))

    return answer
