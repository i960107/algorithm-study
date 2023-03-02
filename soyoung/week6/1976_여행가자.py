import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        return
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
parent = [i for i in range(n+1)]
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if row[j] == 1:
            union_parent(parent, i+1, j+1)
trip = list(map(int, sys.stdin.readline().split()))
for i in range(m-1):
    if find_parent(parent, trip[i]) != find_parent(parent, trip[i+1]):
        print("NO")
        break
else:
    print("YES")