from collections import defaultdict

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
                # 재귀 한 번 끝나고 다시 처음 for문으로 돌아왔을 때 조치를 취해줄 수 있어야 함
                # 반례에서 알파벳 순서대로 갔음에도 ICN -> A -> D -> A 로 재귀가 끝나고 (A에서 더이상 갈 수 있는 곳 x)
                # 돌아올 때 그간 쌓인 result의 길이가 조건을 충족하지 않으면
                # 전체 티켓을 다 사용해 준 게 아니므로 하나씩 재귀 돌면서 append 한 걸 pop해줘야 함
                if len(result) == len(tickets) + 1:
                    return result
                else:
                    result.pop()
                    visited.pop()

    result = ['ICN']
    dfs('ICN')

    return result
