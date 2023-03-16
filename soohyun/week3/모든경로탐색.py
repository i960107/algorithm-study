import copy
from typing import List, Dict


def dfs_iterative(adj: Dict[int, List[int]], start: int, end: int):
    # 모든 경로를 담은 배열
    answer = []

    stack = [start]
    path = []
    visited = [False] * (len(adj) + 1)

    while stack:
        now = stack.pop()
        visited[now] = True
        path.append(now)

        if now == end:
            answer.append(copy.deepcopy(path))

        else:
            cands = []
            for nxt in adj[now]:
                if visited[nxt]:
                    continue
                cands.append(nxt)

            # 갈 수 있는 노드 있다면
            if cands:
                stack.extend(cands)
                continue

        # 백트래킹 지나온 path에 있던 더 살펴볼 필요 없는 노드들 되돌아가기
        # 이미 살펴본 경로 어떻게 제외 시키지. 같은 노드여도 다른 경로를 통해서 방문할 수 있는데
        while path:
            # index에러 난다면 모든 경로 탐색 끝난 것
            path.pop()
            try:
                temp = path[-1]
            except:
                return answer

            arr = []
            # 현재 노드와 연결되어 있는 것 중 현재 경로에 포함되지 않는 원소
            # visited도 False로 되돌려놔야 되는 것 아닌가.
            for nxt in adj[temp]:
                if not visited[nxt]:
                    arr.append(nxt)

            if arr:
                break

    return answer


# 얘시 : 도로 건설
def dfs_recursive(adj: Dict[int, List[int]], now: int, dest: int, path: List[int], visited: List[bool]):
    visited[now] = True
    path.append(now)

    if now == dest:
        answer.append(copy.deepcopy(path))

    else:
        for nxt in adj[now]:
            if visited[nxt]:
                continue
            dfs_recursive(adj, nxt, dest, path, visited)

    path.pop()
    visited[now] = False


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
end = 8

answer = []
path = []
visited = [False] * (9)
dfs_recursive(graph, start, end, path, visited)
print(answer)
result = dfs_iterative(graph, start, end)
print(result)
