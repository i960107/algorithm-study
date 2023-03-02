from collections import deque

n = int(input())

def bfs(flight, v, visited):
    visited.add(v)
    queue = deque([v])
    plane = 0

    while queue:
        c = queue.popleft()

        if len(visited) == len(flight) - 1:
            return plane

        for i in flight[c]:
            if i not in visited:
                plane += 1
                queue.append(i)
                visited.add(i)

for _ in range(n):
    c, f = map(int, input().split())
    flight = [[] for _ in range(c + 1)]  # n번째 인덱스 = n번째 국가에서 갈 수 있는 곳

    for _ in range(f):
        a, b = map(int, input().split())
        flight[a].append(b)
        flight[b].append(a)

    print(bfs(flight, 1, visited=set()))

'''
시간초과 풀이
visited를 set으로 한 부분에서 시간초과가 나는 듯
'''
