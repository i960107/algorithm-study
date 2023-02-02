from typing import List


def solution(distance: int, rocks: List[int], n: int) -> int:
    rocks.sort()

    answer = 0
    # n개의 돌을 징검다리에서 제거 했을때의 최소 거리의 범위.
    lo, hi = 1, distance

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        deleted = 0
        previous = 0
        # n개의 돌을 제거해서 돌 사이의 최소 거리가 mid가 될 수 있는지 확인
        for rock in rocks:
            if rock - previous < mid:
                deleted += 1
            else:
                previous = rock
            # 제거된 돌의 개수가
            if deleted > n:
                break

        # 덜 제거해도 됨.
        if deleted > n:
            hi = mid - 1

        # 꼭 최소 거리의 최대값은 아닐 수 있음
        # elif deleted == n:
        #     answer = mid
        #
        else:
            answer = mid
            lo = mid + 1

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))
