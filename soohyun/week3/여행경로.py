from typing import List, Set, Dict
from collections import defaultdict


def solution(tickets: List[List[str]]) -> List[str]:
    start = "ICN"

    # 인접 행렬로 만들고
    # 티켓 사용 여부 판단하기 위해서 티켓에 id 붙임.
    adj = defaultdict(list)
    for id, (src, dest) in enumerate(tickets):
        adj[src].append((dest, id))

    # 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 하려면
    # 알파벳 순서가 앞서는 경로가 먼저 stack에 추가되어야 함
    for src, dests in adj.items():
        dests.sort()

    # visited[공항]을 하면 안되는 이유 -> tc2에서 처럼 방문한 공항 다시 방문할 수도 있음
    # 주어진 항공권을 모두 사용했는지 체크하기 위해서 쓴 항공권의 id를 set()으로 기록
    # 출발의 경우 티켓이 없이 때문에 -1로 기록. 전체 사용한 항공권의 개수가 n +1 개이면 모든 티켓 사용.
    used = set()
    n = len(tickets)

    path = []
    dfs((start, -1), n, adj, used, path)

    return path


# 반목문으로 처리할 수 있을까?
def dfs(curr, n: int, adj, used: Set[str], path: List[str]) -> bool:
    curr, curr_ticket_id = curr

    if curr_ticket_id in used:
        return False

    used.add(curr_ticket_id)
    path.append(curr)

    if len(used) == n + 1:
        return True

    for next_info in adj[curr]:
        if next_info[0] not in used:
            if dfs(next_info, n, adj, used, path):
                return True

    used.remove(curr_ticket_id)
    path.pop()

    return False


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
