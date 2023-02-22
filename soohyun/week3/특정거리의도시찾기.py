from typing import Dict, List
from collections import defaultdict, deque
from sys import stdin


# 최단 거리가 정확히 K.
# 각 도시와의 최단거리 체크해야함 -> 다익스트라 알고리즘까지 필요할까?
def solution(n: int, m: int, k: int, x: int, adj: Dict[int, List[int]]) -> List[int]:
    queue = deque()
    queue.append((x, 0))
    visited = set()
    cities_in_range = []

    while queue:
        city, distance = queue.popleft()

        if city in visited:
            continue

        visited.add(city)

        if distance > k:
            continue

        if distance == k:
            cities_in_range.append(city)
            continue

        for next in adj[city]:
            queue.append((next, distance + 1))

    return sorted(cities_in_range) if cities_in_range else [-1]


# read로 했더니 debugging할때만 결과 나옴. 백준 runtim error발생
# read는 파일 전체의 내용을 하나의 문자열로 읽어옴
# readline은 한번에 하나의 라인을 읽어오는 메소드
# => read를 하면 eof까지 읽기 때문에 입력이 끝나지 않음
read = stdin.readline

n, m, k, x = map(int, input().split())
adj = defaultdict(list)

for _ in range(m):
    a, b = map(int, read().split())
    adj[a].append(b)

for city in solution(n, m, k, x, adj):
    print(city)
