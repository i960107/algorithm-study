from typing import List


# 방법의 수 X -> 최소 연산 횟수
# 전체 경우의 수를 구한다?
# greedy?
def solution_greedy(n: int) -> List[int]:
    if n == 1:
        return [1]
    if n == 2:
        return [2, 1]

    res = [n]

    for i in range(n, n // 3 * 3, - 1):
        n -= 1
        res.append(n)

    while n != 1:
        n = n // 3
        res.append(n)

    return res


# 시간 초과
def solution_recursive(n: int) -> List[int]:
    if n == 1:
        return [1]
    if n == 2:
        return [2, 1]

    res = []

    # 3으로 나누어떨어지는게 가장 짧은 경로, 2로 나누어 떨어지는 것, 아니면 -1
    if n % 3 == 0:
        case1 = solution_recursive(n // 3)
        if not res or (case1 and len(case1) < len(res)):
            res = case1

    if n % 2 == 0:
        case2 = solution_recursive(n // 2)
        if not res or (case2 and len(case2) < len(res)):
            res = case2

    case3 = solution_recursive(n - 1)
    if not res or len(case3) < len(res):
        res = case3

    return [n] + res


def solution_dp(n: int) -> List[int]:
    if n == 1:
        return [1]
    if n == 2:
        return [2, 1]
    dp = [(i - 1, i - 1) for i in range(n + 1)]
    dp[1] = (0, 1)
    dp[2] = (1, 1)

    # (연산횟수, 바로 이전 수)
    for i in range(1, n + 1):
        if i * 3 <= n and dp[i * 3][0] > dp[i][0] + 1:
            dp[i * 3] = (dp[i][0] + 1, i)

        if i * 2 <= n and dp[i * 2][0] > dp[i][0] + 1:
            dp[i * 2] = (dp[i][0] + 1, i)

        if i + 1 <= n and dp[i + 1][0] > dp[i][0] + 1:
            dp[i + 1] = (dp[i][0] + 1, i)

    answer = [n]
    while True:
        curr = answer[-1]
        if curr == 1:
            break
        answer.append(dp[curr][1])
    return answer


N = int(input())
# solution_greedy가 안되는 이유 -> 53
# 한번 3으로 나누어떨어진다고 그 몫이 3의 배수인 것은 아님.

# solution_recursive가 안되는 이유 -> 10. 당장 2로 나누는 것보다 1을 빼서 3으로 나누는게 더 나음.
res = solution_dp(N)
print(len(res) - 1)
print(*res)
