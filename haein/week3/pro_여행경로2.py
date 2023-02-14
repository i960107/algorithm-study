from collections import defaultdict

# 반례 충족 X
# [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]
# ["ICN", "B", "ICN", "A", "D", "A"]
# 실행한 결괏값 ["ICN","A","D","A","B","ICN"]이 기댓값 ["ICN","B","ICN","A","D","A"]과 다릅니다.
def solution(tickets):
    destinations = defaultdict(list)
    visited = []
    result = []

    ticket_number = 0
    for a, b in tickets:
        ticket_number += 1
        destinations[a].append((b,ticket_number))

    for i in destinations:
        destinations[i].sort(key = lambda x : x[0])

    def dfs(v):
        nonlocal result

        if len(result) == len(tickets) + 1:
            return

        for a, num in destinations[v]:
            if num not in visited:
                result.append(a)
                visited.append(num)
                dfs(a)
                if len(result) == len(tickets) + 1:
                    return result
                else:
                    result = []
                    visited.pop()

    result = ['ICN']
    dfs('ICN')
    print(destinations)
    print(visited)

    return result
