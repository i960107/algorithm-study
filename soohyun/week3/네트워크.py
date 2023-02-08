from typing import List, Dict, Set
from collections import defaultdict, deque


def solution_adj_list(n: int, computers: List[List[int]]) -> int:
    '''인접 리스트로 만든 후 풀이'''
    adj = convert_to_adj_list(n, computers)
    visited = set()

    networks = 0

    for computer in range(n):
        if computer not in visited:
            bfs(adj, computer, visited)
            networks += 1
    return networks


# 파이썬의 모든 data는 객체임
# mutable(list, set, dictionary), immutable(int, tuples, bool, float)객체로 나뉨.
def bfs(adj: Dict[int, List[int]], start: int, visited: Set[int]):
    queue = deque()
    queue.append(start)

    while queue:
        curr = queue.popleft()
        if curr in visited:
            continue
        visited.add(curr)

        for next in adj[curr]:
            queue.append(next)


def convert_to_adj_list(n: int, computers: List[List[int]]) -> Dict:
    adj = defaultdict(list)

    for curr in range(n):
        for next in range(curr + 1, n):
            if computers[curr][next] == 1:
                adj[curr].append(next)
                adj[next].append(curr)
    return adj


def solution_adj_matrix(n: int, computers: List[List[int]]) -> int:
    visited = set()
    networks = 0

    for computer in range(n):
        if computer in visited:
            continue
        bfs_adj_matrix(computers, computer, visited)
        networks += 1

    return networks


def bfs_adj_matrix(adj: List[List[int]], start: int, visited: Set[int]):
    queue = deque()
    queue.append(start)

    while queue:
        curr = queue.popleft()
        if curr in visited:
            continue
        visited.add(curr)

        for next, connected in enumerate(adj[curr]):
            if curr != next and connected:
                queue.append(next)



print(solution_adj_list(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution_adj_list(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
