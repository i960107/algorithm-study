from collections import deque


def solution(f: int, s: int, g: int, u: int, d: int) -> int:
    # 최단거리 -> bfs
    queue = deque()
    queue.append((s, 0))
    visited = [False] * (f + 1)

    while queue:
        floor, buttons = queue.popleft()
        if floor > f or floor < 1:
            continue
        if floor == g:
            return buttons

        if visited[floor]:
            continue

        visited[floor] = True
        queue.append((floor + u, buttons + 1))
        queue.append((floor - d, buttons + 1))
    return -1


f, s, g, u, d = map(int, input().split())
res = solution(f, s, g, u, d)
print(res if res != -1 else 'use the stairs')
