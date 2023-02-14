from collections import defaultdict, deque
def solution(tickets):
    answer = []
    destinations = defaultdict(list)
    visited = []
    result = []

    ticket_number = 0
    for a, b in tickets:
        ticket_number += 1
        destinations[a].append((b,ticket_number))

    for i in destinations:
        destinations[i].sort(key = lambda x : x[0])

    def bfs(v):
        nonlocal result
        queue = deque([v])
        result = [v]

        while queue:
            start = queue.popleft()

            for a, num in destinations[start]: # 하나의 경로를 계속 파고 드는 게 아니라 인접한 것들을 돌면서 visited 처리가 됨
                print(start, a, num, visited, result)
                if num not in visited:
                    result.append(a)
                    visited.append(num)
                    queue.append(a)

    bfs('ICN')
    print(destinations)
    print(result)


    return answer
