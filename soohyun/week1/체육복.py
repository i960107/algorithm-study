from typing import List


def solution(n: int, lost: List[int], reserve: List[int]) -> int:
    uniform = [1] * (n + 2)
    uniform[0] = 0

    for student in lost:
        uniform[student] -= 1

    for student in reserve:
        uniform[student] += 1

    for student in range(1, n):
        if uniform[student] != 2:
            continue

        if uniform[student - 1] == 0:
            uniform[student - 1], uniform[student] = 1, 1
            continue

        if uniform[student + 1] == 0:
            uniform[student + 1], uniform[student] = 1, 1

    return sum([1 for count in uniform if count >= 1])


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
