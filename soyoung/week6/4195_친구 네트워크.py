import sys
sys.setrecursionlimit(10**5)
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

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]
for i in range(m):
    num, a, b = map(int, sys.stdin.readline().split())
    if num == 0:
        union_parent(parent, a, b)
    elif num == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")