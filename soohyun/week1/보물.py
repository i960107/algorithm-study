from typing import List
from functools import reduce


def solution(n: int, A: List[int], B: List[int]) -> int:
    A.sort()
    B.sort(reverse=True)

    s = 0
    for a, b in zip(A, B):
        s += (a * b)

    return s


def solution_functool(n: int, A: List[int], B: List[int]) -> int:
    A.sort()
    B.sort(reverse=True)

    return reduce(lambda x, y: (x + y), [a * b for a, b in zip(A, B)], 0)


n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solution_functool(n, A, B))
