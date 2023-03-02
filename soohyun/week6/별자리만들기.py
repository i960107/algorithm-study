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


N = int(input())
parent = [i for i in range(1 + N)]

coords = []
distances = []
for _ in range(N):
    x, y = map(float, input().split())
    coords.append((x, y))
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        distance = round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 2)
        distances.append((distance, i + 1, j + 1))

distances.sort()

total_distance = 0

for distance, a, b in distances:
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        continue
    union(parent, a, b)
    total_distance += distance

print(total_distance)
