from typing import List
from collections import defaultdict


# 임의의 서로 다른 두 방 사이의 최단 경로는 딱 한가지 -> 무슨 말?
def solution(n, path, order):
    adj = defaultdict(list)
    for a, b in path:
        adj[a].append(b)
        adj[b].append(a)

    required = dict()
    for a, b in order:
        if b == 0:
            return False
        required[b] = a

    stk = [0]
    visited = set()

    to_visit = defaultdict(list)

    while stk:
        now = stk.pop()
        if now in required and required[now] not in visited:
            to_visit[required[now]] = now
            continue
        print(now)
        visited.add(now)
        for nxt in adj[now]:
            if nxt not in visited:
                stk.append(nxt)
        # 먼저 방문해야 하는 것들 먼저 방문
        if now in to_visit:
            stk.append(to_visit[now])

    if len(visited) != n:
        return False

    return True


def solution_fail(n, path, order):
    answer = False
    adj = defaultdict(list)
    # 여기서 우선순위 조정해주지 않는 이유 -> 다른 노드를 거쳐서 a -> b 로 가는 것도 막기 위해서는 매번 우선순위 체크 해주어야하기 때문
    for a, b in path:
        adj[a].append(b)
        adj[b].append(a)

    # key를 방문하기 위해서는 room을 방문해야 함
    # 각 우선순위는 서로 관련이 없음. 독립적인 조건
    required = dict()
    for a, b in order:
        required[b] = a

    def dfs(now, visited):
        if now in visited:
            return False

        visited.add(now)

        if len(visited) == n:
            return True

        for nxt in adj[room]:
            # 우선순위 체크
            # nxt를 방문하기 전에 먼저 방문해야 하는 노드
            if nxt in required and required[nxt] not in visited:
                continue
            if dfs(nxt, visited):
                return True

        visited.remove(now)
        return False

    # 방문했던 노드 또 방문해도 됨! 단순히 dfs아님. -> maximum recursion limit exceed
    # 입구는 항상 0
    start = [room for room in range(n) if room not in required]
    for room in start:
        visited = set()
        if dfs(room, visited):
            return True
    return False


print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]))
