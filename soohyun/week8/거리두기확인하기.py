from typing import List
from collections import deque


def solution(places: List[List[str]]) -> List[int]:
    answer = []
    for place in places:
        result = _solution(place)
        answer.append(int(result))
    return answer


# 테스트 5만 실패
def _solution(place: List[str]) -> bool:
    n = 5
    dr = (0, 0, 1, -1)
    dc = (-1, 1, 0, 0)

    PARTITION = "X"
    PERSON = "P"
    EMPTY = "O"

    def bfs(r: int, c: int) -> bool:
        queue = deque()
        queue.append((r, c, 0))

        while queue:
            cr, cc, distance = queue.popleft()

            if distance == 2:
                continue

            for k in range(4):
                nr, nc, ndistance = cr + dr[k], cc + dc[k], distance + 1
                if not (0 <= nr < n and 0 <= nc < n):
                    continue
                # 파티션이면 continue해도 되는 이유.
                # 둘 응시자 사이의 거리가 2인 경로 중에 partition이 아닌 곳이 있다면 그 경로에서 체크될 것
                if visited[nr][nc]:
                    continue
                visited[nr][nc] = True

                if place[nr][nc] == PARTITION:
                    continue

                if place[nr][nc] == PERSON:
                    return False
                queue.append((nr, nc, ndistance))

        return True

    # visited타이밍이 중요!
    visited = [[False] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if visited[r][c]:
                continue
            # 빈 테이블인데 방문체크해버리면 에러...
            # visited[r][c] = True
            # 사람인 곳으로부터 길이가 2인 곳까지 체크.
            # 단순히 방문체크하면 안됨. -> bfs로 체크한 곳만 방문 체크.
            if place[r][c] != PERSON:
                continue
            visited[r][c] = True
            if not bfs(r, c):
                return False
    return True


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
