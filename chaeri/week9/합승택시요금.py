def solution(n, s, a, b, fares):
    INF = 10000000
    answer = INF
    graph = [[INF] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0

    for f in fares:
        node1, node2, fee = f
        graph[node1 - 1][node2 - 1] = fee
        graph[node2 - 1][node1 - 1] = fee

    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for t in range(n):
        temp = graph[s - 1][t] + graph[t][a - 1] + graph[t][b - 1]
        answer = min(temp, answer)

    return answer