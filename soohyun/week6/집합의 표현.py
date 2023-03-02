from typing import List
from sys import stdin
import sys


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


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

sys.setrecursionlimit(10 ** 6)
read = stdin.readline

# 0 <= a, b <= n
for _ in range(m):
    op, a, b = map(int, read().split())
    if op == 0:
        union(parent, a, b)
    else:
        group_a = find(parent, a)
        group_b = find(parent, b)
        print("YES" if group_a == group_b else "NO")
