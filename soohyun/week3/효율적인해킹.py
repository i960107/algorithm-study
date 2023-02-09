from typing import List, Dict, Set
from collections import defaultdict, deque
from sys import stdin


# 어떻게 하면 시간을 줄일 수 있을까?
def solution_dp(n: int, m: int, friends: List[List[int]]) -> List[int]:
    target = []
    max_hacked = 0
    # 한번 탐색한 경로는 탐색할 필요 없음 -> hackable(각 컴퓨터로부터 해킹할 수 있는 컴퓨터의 수)을  기록
    hackable = [None] * (n + 1)
    for start in range(1, n + 1):
        hacked = dfs(friends, start, hackable)
        if len(hacked) > max_hacked:
            target, max_hacked = [start], len(hacked)
        elif len(hacked) == max_hacked:
            target.append(start)
        hackable[start] = hacked
    return sorted(target)


def dfs(friends: List[List[int]], start: int, hackable: List[Set[int]]) -> Set[int]:
    stack = []
    stack.append(start)

    hacked = set()

    while stack:
        curr = stack.pop()

        if curr in hacked:
            continue

        hacked.add(curr)
        # 이미 탐색한 적 있다면 dfs 중지.
        # 이미 탐색한 곳이라도 탐색해야함. visited를 udpate할 수 없기 때문에
        if hackable[curr]:
            hacked.update(hackable[curr])
            continue

        for next in friends[curr]:
            stack.append(next)

    return hacked


def solution_test(n: int, m: int, friends: List[List[int]]) -> List[int]:
    hacked = [-1] * (n + 1)
    for computer in range(1, n + 1):
        hacked[computer] = count_hacked(n, friends, computer)

    max_hacked = max(hacked)
    return [computer for computer in range(1, n + 1) if hacked[computer] == max_hacked]


def count_hacked(n: int, friends: List[List[int]], start: int) -> int:
    visited = [False] * (n + 1)
    queue = deque()

    visited[start] = True
    queue.append(start)

    count = 1
    while queue:
        curr = queue.popleft()
        for next in friends[curr]:
            if visited[next]:
                continue
            visited[next] = True
            count += 1
            queue.append(next)
    return count


read = stdin.readline
n, m = map(int, input().split())
friends = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, read().split())
    friends[b].append(a)

print(*solution_dp(n, m, friends))
