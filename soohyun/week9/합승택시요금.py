from typing import List


def solution(n: int, s: int, a: int, b: int, fares: List[List[int]]) -> int:
    INF = int(1e9)

    # 플루이드 워셜은 노드의 개수가 500 개 이하힐때 적합한 방법? O(N^3)
    distance = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        distance[i][i] = 0

    for u, v, w in fares:
        distance[u][v] = w
        distance[v][u] = w

    for k in range(1, n + 1):
        # 이전에 정해진 값들을 참조
        for u in range(1, n + 1):
            for v in range(1, n + 1):
                distance[u][v] = min(distance[u][v], distance[u][k] + distance[k][v])

    final_fare = INF
    for k in range(1, n + 1):
        # s == k인 경우 합승을 하지 않는 경우의 수
        common = distance[s][k]
        a_fare = distance[k][a]
        b_fare = distance[k][b]

        if common + a_fare + b_fare < final_fare:
            final_fare = common + a_fare + b_fare
    for row in distance:
        print(row)
    return final_fare


print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
