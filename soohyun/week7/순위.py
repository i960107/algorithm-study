from typing import List


def solution(N: int, results: List[List[int]]) -> int:
    wins = [[None] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        wins[i][i] = False

    for winner, loser in results:
        wins[winner][loser] = True
        wins[loser][winner] = False

    # 선수가 100명 이하이기 때문에 O(N^3)복잡도의 플로이드 워셜 알고리즘 적용 가능
    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                # 방향이 일관되기만 하면 됨.
                if wins[a][k] and wins[k][b]:
                    wins[a][b] = True

                if wins[a][k] == False and wins[k][b] == False:
                    wins[a][b] = False

    count = 0
    for a in range(1, N + 1):
        defined = True
        for b in range(1, N + 1):
            res = wins[a][b]
            if res is None:
                defined = False
                break
        if defined:
            count += 1
    return count


# 이 풀이는 대체 왜 되는 거야..
def solution2(N: int, results: List[List[int]]) -> int:
    INF = int(1e9)
    wins = [[INF] * (N + 1) for _ in range(N + 1)]

    # 거리로 해볼까
    for i in range(1, N + 1):
        wins[i][i] = 0

    for winner, loser in results:
        # 양방향으로 설정해주면 안됨..
        wins[winner][loser] = 1
        # wins[loser][winner] = 1

    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                wins[a][b] = min(wins[a][b], wins[a][k] + wins[k][b])

    for row in wins:
        print(row)

    result = 0
    for a in range(1, N + 1):
        count = 0
        for b in range(1, N + 1):
            # wins[a][b] == wins[b][a]
            if wins[a][b] != INF or wins[b][a] != INF:
                count += 1
        if count == N:
            result += 1
    return result


print(solution2(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
