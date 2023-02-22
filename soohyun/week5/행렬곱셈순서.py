from typing import List, Tuple


def get_min_multiplication(left_most: int, right_most: int) -> int:
    # 이런 경우가 있나?
    if left_most < 0 or right_most >= N or left_most > right_most:
        return 500 * 500 * 500 + 1

    if dp[left_most][right_most] != -1:
        return dp[left_most][right_most]

    min_operations = 500 * 500 * 500 + 1
    # 연산 횟수와 연산 결과 둘다 필요하지 않나?
    # 연산 결과는 필요없음. matrix에서 연산 몇 번 필요한지 조회할 수 있음
    for mid in range(left_most, right_most):
        # 만약 dp값이 아직 없으면? top - down방식으로 구해야함. -> 재귀밖에 없나?
        # 앞에서부터 찾아가는 경우에는 반복문으로 구할 수 있지만 부분 문제로 쪼개어 가는 경우 재귀뿐!
        left_operation = get_min_multiplication(left_most, mid)
        right_operation = get_min_multiplication(mid + 1, right_most)
        total_operation = left_operation \
                          + right_operation \
                          + (matrix[left_most][0] * matrix[mid][1] * matrix[right_most][1])
        min_operations = min(total_operation, min_operations)
    dp[left_most][right_most] = min_operations
    return min_operations


def is_multiplicable(matrix: List[Tuple[int, int]]) -> bool:
    for i in range(1, len(matrix)):
        r1, c1 = matrix[i - 1]
        r2, c2 = matrix[i]
        if c1 != r2:
            return False
    return True


N = int(input())
matrix = []
for _ in range(N):
    r, c = map(int, input().split())
    matrix.append((r, c))

dp = [[-1] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0

print(get_min_multiplication(0, N - 1))
