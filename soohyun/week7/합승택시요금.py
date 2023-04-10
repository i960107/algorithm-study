from typing import List


def solution(n: int, s: int, a: int, b: int, fares: List[List[int]]) -> int:
    # s -> a, 각각은  s->b까지 가는 최단 거리는 다익스트라로 구할 수 있음
    INF = int(1e9)

    distance = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        distance[i][i] = 0

    for u, v, f in fares:
        distance[u][v] = f
        distance[v][u] = f

    for k in range(1, n + 1):
        for u in range(1, n + 1):
            for v in range(1, n + 1):
                original = distance[u][v]
                new = distance[u][k] + distance[k][v]
                if new < original:
                    distance[u][v] = new
    final_fare = INF
    for k in range(1, n + 1):
        common = distance[s][k]
        a_fare = distance[k][a]
        b_fare = distance[k][b]
        total_fare = common + a_fare + b_fare
        if total_fare < final_fare:
            final_fare = total_fare
    return final_fare


print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))
