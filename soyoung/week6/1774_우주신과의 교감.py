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

n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
points = []  # 우주인의 좌표
edges = []  # 간선 정보
ans = 0
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))
idx1, idx2 = map(int, sys.stdin.readline().split())
union_parent(parent, idx1, idx2)
# edges.append((math.sqrt((points[idx1-1][0] - points[idx2-1][0])**2 + (points[idx1-1][1] - points[idx2-1][1])**2), idx1-1, idx2-1))
for i in range(n-1):
    for j in range(i+1, n):
        # 간선에 (cost, i, j) 붙이기
        edges.append((math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2), i, j))
edges.sort()
print(edges)
for i in range(len(edges)):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        ans += cost
print(round(ans, 2))