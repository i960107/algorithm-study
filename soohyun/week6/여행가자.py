from typing import List
from sys import stdin


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
N = int(input())
M = int(input())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
parent = [i for i in range(N + 1)]

places = list(map(int, input().split()))

for a in range(N):
    for b in range(N):
        if grid[a][b]:
            union(parent, a + 1, b + 1)

group_id = -1
possible = True
for place in places:
    if group_id == -1:
        group_id = find(parent, place)
        continue
    if find(parent, place) != group_id:
        possible = False
        break

print("YES" if possible else "NO")
