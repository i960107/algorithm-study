# 참고 풀이 https://life318.tistory.com/4
def solution(n, results):
    answer = 0

    INF = int(1e9)

    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for a, b in results:
        graph[a][b] = 1 # a가 b를 이김

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if graph[a][k] == graph[k][b] == 1:
                    graph[a][b] = 1

    for a in range(1, n+1):
        sum_row = sum(graph[a]) # a번 선수가 확실하게 이기는 선수 수
        sum_col = 0
        for b in range(1, n+1):
            sum_col += graph[b][a] # a번 선수가 확실하게 지는 선수 수
        if sum_row + sum_col == n-1: # 확실하게 이기거나 지는 선수 수가 n-1일 때 등수 확실
            answer += 1

    return answer



'''
위상정렬은 모든 등수가 확실해야 한다. 
플루이드 워셜 알고리즘을 통해 순서에 맞춰서 모든 노드에 방문해서 모든 정점 사이의 최단 경로를 찾을 수 있다.

from collections import deque
def solution(n, results):
    answer = 0
    indegree = [0] * (n+1)
    graph = [[] for i in range(n+1)]

    for a, b in results:
        graph[a].append(b)
        indegree[b] += 1

    def topology_sort():
        result = []
        q = deque()

        cnt = 0
        for i in range(1, n+1):
            if indegree[i] == 0:
                cnt += 1
        if cnt > 1:
            for i in range(1, n+1):
                if indegree[i] == 0:
                    q.append((i, 1)) # 확실하지 않은 케이스 1
        else:
            for i in range(1, n+1):
                if indegree[i] == 0:
                    q.append((i, 0)) # 확실한 케이스

        while q:
            now, cer = q.popleft()
            result.append((now, cer))
            cnt = 0
            for i in graph[now]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    i
                    cnt += 1
            if cnt > 1:
                for i in graph[now]:
                    if indegree[i] == 0:
                        q.append((i, 1))
            else:
                for i in graph[now]:
                    if indegree[i] == 0:
                        q.append((i, 0))

        return result

    return topology_sort()

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
'''
