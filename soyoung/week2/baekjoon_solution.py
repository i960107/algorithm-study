import sys

M, N, L = map(int, sys.stdin.readline().split())
locations = sorted(list(map(int, sys.stdin.readline().split())))
animals = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
animals.sort(key=lambda x:(x[0],x[1]))
cnt = 0
start, end = 0, M-1

for i in animals:
    min_x = float('inf')
    if i[1] > L: continue
    for x in locations:
        if abs(x - i[0]) < min_x:
            min_x = abs(x - i[0])

