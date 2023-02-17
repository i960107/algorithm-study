from typing import List


# dfs를 총 세가지 방법으로 풀이. O(N!), 8! = 40320 가능.
# 1) solution_dfs_iterative: dfs 반복문 버전.
# 2) solution_dfs_recursive: dfs 재귀 버전(재귀 호출 후 방문처리) -> 가장 좋은 방법
# 3) solution_dfs_recursive_version2: dfs 재귀 버전(재귀 호출 전 방문 처리)


def solution_dfs_iterative(k: int, dungeons: List[List[int]]) -> int:
    max_dungeons = 0
    for dungeon in range(len(dungeons)):
        res = dfs_iterative(dungeon, k, dungeons)
        max_dungeons = max(max_dungeons, res)
    return max_dungeons


# 재귀가 아니고서야 visited를 어떻게 처리하는게 좋을까?
# -> 경로마다 visited를 관리해주기. -> 메모리 많이 필요하므로 재귀가 더 나은 방법!
def dfs_iterative(start: int, k: int, dungeons: List[List[int]]) -> int:
    if k < dungeons[start][0]:
        return 0

    n = len(dungeons)

    stack = []
    stack.append((start, [False] * n, k, []))
    max_dungeons = 0
    while stack:
        curr, visited, left, path = stack.pop()
        required, consume = dungeons[curr]

        visited[curr] = True
        left -= consume
        path.append(curr)

        for dungeon in range(n):
            if visited[dungeon] or dungeons[dungeon][0] > left:
                max_dungeons = max(max_dungeons, sum(visited))
                continue
            stack.append((dungeon, visited.copy(), left, path.copy()))

    return max_dungeons


# 모든 경로를 탐색하는 것까진 된 거 같은데... 어떤 값을 언제 반환해야할까?
# 모든 경로 중 최대 값을 반환해야 하는데.
# 재귀 함수 들어오면서 방문처리를 해준다. 호출한다고 방문한것 아님 -> 처음 dfs를 호출하는 곳에서 방문처리 안 해줘도 됨


def dfs_recursive(curr: int, k: int, dungeons: List[List[int]], visited: List[bool]) -> int:
    visited[curr] = True
    k -= dungeons[curr][1]

    max_dungeon_after = 0
    for dungeon in range(len(dungeons)):
        if visited[dungeon]:
            continue
        if dungeons[dungeon][0] > k:
            continue

        max_dungeon_after = max(max_dungeon_after, dfs_recursive(dungeon, k, dungeons, visited))

    visited[curr] = False
    k += dungeons[curr][1]

    return max_dungeon_after + 1


def solution_dfs_recursive_version2(k: int, dungeons: List[List[int]]) -> int:
    max_dungeons = 0
    for dungeon in range(len(dungeons)):
        if dungeons[dungeon][0] > k:
            continue
        visited = [False] * len(dungeons)

        visited[dungeon] = True
        k -= dungeons[dungeon][1]

        res = dfs_recursive_version2(k, dungeons, visited)
        max_dungeons = max(max_dungeons, res)
    return max_dungeons

    # 방문 처리를 stack에 넣으면서 해준다 -> 처음 dfs함수를 호출하는 곳에서도 방문처리를 해줘야해서 실수할 확률 올라감!


def dfs_recursive_version2(k: int, dungeons: List[List[int]], visited: List[bool]) -> int:
    max_dungeon_after = 0
    for dungeon in range(len(dungeons)):
        if visited[dungeon] or dungeons[dungeon][0] > k:
            continue

        visited[dungeon] = True
        k -= dungeons[dungeon][1]

        max_dungeon_after = max(max_dungeon_after, dfs_recursive_version2(k, dungeons, visited))

        visited[dungeon] = False
        k += dungeons[dungeon][1]

    return max_dungeon_after + 1


print(solution_dfs_iterative(80, [[80, 20], [50, 40], [30, 10]]))
print(solution_dfs_recursive_version2(80, [[80, 20], [50, 40], [30, 10]]))
