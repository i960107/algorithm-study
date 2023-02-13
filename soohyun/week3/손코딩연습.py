from typing import List, Dict, Set, Tuple, Deque
from collections import deque


def bfs(adj: Dict[int, List[int]], start: int) -> List[int]:
    queue = deque()
    visited_nodes = []
    visited = set()

    # (node, distance)로 저장
    queue.append((start, 0))

    while queue:
        curr, distance = queue.popleft()

        if curr in visited:
            continue

        visited_nodes.append(curr)
        visited.add(curr)

        for next in adj[curr]:
            queue.append((next, distance + 1))

    return visited_nodes


def bfs_version2(adj: Dict[int, List[int]], start: int) -> List[int]:
    # 해인 버전
    queue = deque()
    visited_nodes = []
    visited = set()

    # (node, distance)로 저장
    visited[start] = True
    queue.append((start, 0))
    # 주의! queue에 삽입하기 전에 방문처리

    while queue:
        curr, distance = queue.popleft()

        if curr in visited:
            continue

        visited_nodes.append(curr)
        visited.add(curr)

        for next in adj[curr]:
            queue.append((next, distance + 1))

    return visited_nodes


def dfs_recursive(adj: Dict[int, List[int]], node: int, visited: Set[int]) -> List[int]:
    if node in visited:
        return []

    visited.add(node)
    visited_nodes = [node]

    for index in range(len(adj[node]) - 1, -1, -1):
        visited_nodes.extend(dfs_recursive(adj, adj[node][index], visited))

    return visited_nodes


def dfs_iterative(adj: Dict[int, List[int]], start: int) -> List[int]:
    stack = []
    visited = set()
    visited_nodes = []
    stack.append((start, 0))

    while stack:
        curr, distance = stack.pop()

        if curr in visited:
            continue

        visited_nodes.append(curr)
        visited.add(curr)

        for next in adj[curr]:
            stack.append((next, distance + 1))

    return visited_nodes


graph = {
    1: [2, 3, 8],
    2: [1, 7],
    3: [1, 4, 5],
    4: [3, 5],
    5: [3, 4],
    6: [7],
    7: [2, 6, 8],
    8: [1, 7]
}

start = 1

# 1 -> 2 -> 3 -> 8 -> 7 -> 4 -> 6
# print(bfs(graph, start))
# 1 -> 8 -> 7-> 6-> 2-> 3 -> 5-> 4
print(dfs_recursive(graph, 1, set()))
print(dfs_iterative(graph, start))
