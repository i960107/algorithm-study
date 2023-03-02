import sys
import math

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if b > a:
        parent[b] = a
    else:
        parent[a] = b

n = int(sys.stdin.readline())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
stars = []  # 별의 좌표
edges = []  # 간선 정보
ans = 0
for i in range(n):
    x, y = map(float, sys.stdin.readline().split())
    stars.append((x, y))

for i in range(n-1):
    for j in range(i+1, n):
        # 간선에 (cost, i, j) 붙이기
        edges.append((math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2), i, j))
edges.sort()

for i in range(len(edges)):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        ans += cost
print(round(ans, 2))