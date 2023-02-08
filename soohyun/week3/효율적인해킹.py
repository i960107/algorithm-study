from typing import List, Dict
from collections import defaultdict
from sys import stdin


# 어떻게 하면 시간을 줄일 수 있을까?
def solution(n: int, m: int, friends: Dict[int, List[int]]) -> List[int]:
    target = []
    max_hacked = 0
    # 한번 탐색한 경로는 탐색할 필요 없음 -> hackable(각 컴퓨터로부터 해킹할 수 있는 컴퓨터의 수)을  기록
    hackable = [-1] * (n + 1)
    for start in range(1, n + 1):
        hacked = dfs(friends, start, hackable)
        if hacked > max_hacked:
            target, max_hacked = [start], hacked
        elif hacked == max_hacked:
            target.append(start)
        hackable[start] = hacked
    return sorted(target) if target else [-1]


def dfs(friends: Dict[int, List[int]], start: int, hackable: List[int]) -> int:
    stack = []
    stack.append(start)

    visited = set()

    hacked = 0

    while stack:
        curr = stack.pop()

        if curr in visited:
            continue

        visited.add(curr)

        # 이미 탐색한 적 있다면 dfs 중지.
        if hackable[curr] != -1:
            hacked += hackable[curr]
            continue

        hacked += 1
        for next in friends[curr]:
            stack.append(next)

    return hacked


def solution_test(n: int, m: int, friends: Dict[int, List[int]]) -> List[int]:
    max_count = 0
    targets = []
    for computer in range(1, n + 1):
        count = count_hacked(n, friends, computer)
        if count > max_count:
            max_count, targets = count, [computer]
        elif count == max_count:
            targets.append(computer)
    return sorted(targets) if targets else [-1]


def count_hacked(n: int, freinds: List[int], start: int) -> int:
    stack = []
    stack.append(start)

    visited = [False] * (n + 1)
    count = 0
    while stack:
        curr = stack.pop()
        if visited[curr]:
            continue
        visited[curr] = True
        count += 1
        for next in friends[curr]:
            stack.append(next)
    return count


read = stdin.readline
n, m = map(int, input().split())
friends = defaultdict(list)
for _ in range(m):
    a, b = map(int, read().split())
    friends[b].append(a)

print(*solution_test(n, m, friends))
