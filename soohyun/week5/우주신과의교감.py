from sys import stdin
from typing import List, Tuple


def find(parent: List[int], x: int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent: List[int], a: int, b: int):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


read = stdin.readline
N, M = map(int, read().split())

parent = [i for i in range(N + 1)]

gods = [(-1, -1)]
for _ in range(N):
    x, y = map(int, read().split())
    gods.append((x, y))

for _ in range(M):
    x, y = map(int, read().split())
    union(parent, x, y)

# 이미 연결되어 있는 곳도 다 넣어줌 -> 어차피 cycle형성 체크에서 걸러짐
distances = []
for i in range(1, N + 1):
    r1, c1 = gods[i]
    for j in range(1, N + 1):
        if i == j:
            continue
        r2, c2 = gods[j]
        distance = ((r2 - r1) ** 2 + (c2 - c1) ** 2) ** 0.5
        distances.append((distance, i, j))

# 크루스칼 알고리즘
distances.sort()
total_distance = 0

for distance, i, j in distances:
    i = find(parent, i)
    j = find(parent, j)
    if i == j:
        continue
    total_distance += distance
    union(parent, i, j)

print(f'%.2f' % total_distance)
