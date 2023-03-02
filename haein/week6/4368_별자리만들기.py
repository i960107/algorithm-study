import math

def find_parent(x):
    if parent[x] != x: # 루트노드를 찾기 위해! 루트노드는 자기 자신과 같음
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [i for i in range(n+1)]

stars = []
edges = []
result = 0

for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))

for i in range(n-1):
    for j in range(i+1, n):
        edges.append((math.sqrt((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2), i, j))

edges.sort()

for edge in edges:
    cost, x, y = edge

    if find_parent(x) != find_parent(y): # 사이클 형성 X, 만약 사이클 형성하면 result에 안 담음!
        union_parent(x, y)
        result += cost

print(round(result, 2))
