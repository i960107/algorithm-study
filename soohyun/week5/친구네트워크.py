from sys import stdin
from collections import defaultdict
from typing import List, Dict


# dfs
# union-find의 경우 친구 이름 -> index로 치환하기 어려움. 사람의 수 알 수 없어서 곤란
# dfs로만 하니 시간 초과남. 친구 최대 100,000. 각 dfs 최대 100,000 => 총 100,000,000,000.
# 네트워크별 개수를 저장해둬야겠음.
# def dfs(friends: Dict[str, List[str]], start: str) -> int:
#     network = []
#     stack = []
#     stack.append(start)
#     visited = set()
#
#     while stack:
#
#         curr = stack.pop()
#
#         if curr in visited:
#             continue
#
#         network.append(curr)
#         visited.add(curr)
#
#         for next in friends[curr]:
#             stack.append(next)
#
#     return len(network)

def find(parent: Dict[str, str], x: str) -> str:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


# 부모 노드 번호를 Return함
def union(parent: Dict[str, str], a: str, b: str, networks: Dict[str, int]):
    a = find(parent, a)
    b = find(parent, b)

    # 중복으로 count 됨. a== b여도 합침?
    # if a < b:
    #     parent[b] = a
    #     networks[a] = networks.get(a, 1) + networks.get(b, 1)
    #     print(networks[a])
    # elif a > b:
    #     parent[a] = b
    #     networks[b] = networks.get(a, 1) + networks.get(b, 1)
    #     print(networks[b])
    if a == b:
        return

    parent[b] = a
    networks[a] += networks[b]
    print(networks[a])


def get_group_size(groups: Dict[str, str], target: str) -> int:
    count = 0
    target = find(groups, target)
    for k, v in groups.items():
        if find(groups, v) == target:
            count += 1
    return count


read = stdin.readline
T = int(read())
for _ in range(T):
    F = int(read())
    groups = defaultdict(str)
    networks = defaultdict(int)
    for _ in range(F):
        a, b = read().split()

        if a not in groups:
            groups[a] = a
            networks[a] = 1

        if b not in groups:
            groups[b] = b
            networks[b] = 1

        union(groups, a, b, networks)
