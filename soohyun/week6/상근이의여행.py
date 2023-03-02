from sys import stdin
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


# 연결 그래프: 모든 두 꼭짓점 사이에 경로가 존재하는 그래프
# 모든 꼭지점에서 DFS를 통해 다 탐색하는 것? 이미 방문한 노드를 방문해도 됨... 가짓수 너무 많
# 종류는 구하는 것

read = stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    parent = [i for i in range(N + 1)]
    for _ in range(M):
        a, b = map(int, read().split())
        union(parent, a, b)
    print(N - 1)
