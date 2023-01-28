from typing import List


def solution(n: int, l: int, holes: List[int]) -> int:
    # 정렬되지 않은 위치가 주어질 수 있단는 것 주의!
    holes.sort()
    tape_used = 0
    taped = 0

    for hole in holes:
        if taped < hole:
            tape_used += 1
            taped = hole + l - 1
    return tape_used


n, l = map(int, input().split())
holes = list(map(int, input().split()))
print(solution(n, l, holes))
