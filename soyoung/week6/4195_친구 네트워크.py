import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        number[a] += number[b]
    print(number[a])

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    parent, number = {}, {}
    for i in range(n):
        a, b = map(str, sys.stdin.readline().split())
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        union(a,b)



