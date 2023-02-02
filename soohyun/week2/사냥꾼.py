from typing import List, Tuple
from sys import stdin


def solution(m: int, n: int, l: int, haunters: List[int], animals: List[Tuple[int]]) -> int:
    # 정렬을 어떤 순으로 해야 할까?
    # 헌터의 입장에서 사정 거리내 동물들의 수를 찾아보기
    # 동물의 입장에서 사정거리 내 헌터 있는지 찾아보기
    # bfs로 찾아봐도 되지 않을까? -> 좌표값이 너무 커서 시간 초과 발생할 것
    haunters.sort()
    cnt = 0

    for x, y in animals:
        if y > l:
            continue
        start, end = x + y - l, x - y + l
        left, right = 0, m - 1
        while left <= right:
            mid = left + (right - left) // 2
            # 동물을 잡을 수 있는 사정 거리 안에 있는지 확인
            if start <= haunters[mid] <= end:
                cnt += 1
                break
            # 여기가 이해가 잘 안 됨.
            elif haunters[mid] < start:
                left = mid + 1
            else:
                right = mid - 1

    return cnt


def solution_practice(m: int, n: int, l: int, haunters: List[int], animals: List[int]) -> int:
    haunters.sort()
    count = 0
    for x, y in animals:
        if y > l:
            continue
        start, end = x + y - l, x - y + l
        lo, hi = 0, len(haunters)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if start <= haunters[mid] <= end:
                count += 1
                break
            if haunters[mid] < start:
                lo = mid + 1
            else:
                hi = mid - 1
    return count


m, n, l = map(int, input().split())
haunters = list(map(int, input().split()))
read = stdin.readline
animals = []
for _ in range(n):
    animals.append(tuple(map(int, read().split())))

print(solution(m, n, l, haunters, animals))
