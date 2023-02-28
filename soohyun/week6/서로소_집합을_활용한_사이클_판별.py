from typing import List


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


v, e = map(int, input().split())

parent = [i for i in range(v + 1)]
cycle = False
for _ in range(e):
    a, b = map(int, input().split())
    a = find(parent, a)
    b = find(parent, b)

    if a == b:
        cycle = True
        break
    union(parent, a, b)

if cycle:
    print('cycle 발생')
else:
    print('cycle 발생 안함')
