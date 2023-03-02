from typing import List, Tuple
from sys import stdin
from collections import defaultdict, deque


def solution(n: int, previous_ranks: List[int], m: int, changed: List[Tuple[int, int]]):
    indegree = [0] * (n + 1)
    d = defaultdict(set)

    for i in range(n):
        team = previous_ranks[i]
        for j in range(i + 1, n):
            next = previous_ranks[j]
            # indegree는 직접적으로 들어오는 차수 아니고 간접적으로 들어오는 차수까지 포함함.
            indegree[next] += 1
            d[team].add(next)

    for i, j in changed:
        if j in d[i]:
            indegree[j] -= 1
            indegree[i] += 1
            d[i].remove(j)
            d[j].add(i)
        else:
            indegree[i] -= 1
            indegree[j] += 1
            d[j].remove(i)
            d[i].add(j)

    queue = deque()
    for team in range(1, n + 1):
        if indegree[team] == 0:
            queue.append(team)

    # 불가능한 경우와 불확실한 경우
    # indegree가 이미 0인데 빼줘야하는 경우, 사이클이 생기는 경우.?
    # 확실한 순위를 찾을 수 없는 경우가 있나?
    # 진입차수를 또 빼주는 경우는 없다.
    ranks = []
    while queue:
        curr = queue.popleft()
        ranks.append(curr)
        for next in d[curr]:
            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(next)

    if not ranks or len(ranks) != n:
        print('IMPOSSIBLE')
    else:
        print(*ranks)


read = stdin.readline
T = int(input())
for _ in range(T):
    n = int(read())

    previous_rank = list(map(int, read().split()))

    m = int(read())
    changed = []
    for _ in range(m):
        a, b = map(int, read().split())
        changed.append((a, b))

    solution(n, previous_rank, m, changed)
