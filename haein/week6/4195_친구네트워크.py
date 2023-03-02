import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

def find_parent(parent, x):
    if parent[x] != [x]:
        parent[x] = find_parent(parent, parent[x][0])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)[0]
    b = find_parent(parent, b)[0]

    if a < b:
        parent[b] = [a]
    else:
        parent[a] = [b]

for _ in range(n):
    c = int(input())
    parent = defaultdict(list)

    for _ in range(c):
        a, b = input().split()
        if a not in parent:
            parent[a] = [a]
        if b not in parent:
            parent[b] = [b]
        union_parent(parent, a, b)

        pa = find_parent(parent, a)
        pb = find_parent(parent, b)

        count = 0
        for i in parent.keys():
            tmp_res = find_parent(parent, i)
            if tmp_res == pa:
                count += 1

        print(count)


        # for i in [a, b]:
        #     count = 0
        #     root = find_parent(parent, i)
        #     for j in parent.values():
        #         if root == j:
        #             count += 1
        #     print(count)



