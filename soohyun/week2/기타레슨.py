from typing import List


def solution(n: int, m: int, lectures: List[int]) -> int:
    # lo, hi의 범위
    lo, hi = 1, sum(lectures)
    # lo, hi = max(lectures), sum(lectures)
    answer = 0
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if can_record_in_length(mid, m, lectures):
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1

    return answer


def can_record_in_length(length: int, m: int, lectures: List[int]) -> bool:
    count = 0
    temp = []
    for lecture in lectures:
        if not temp or temp[-1] + lecture > length:
            count += 1
            temp.append(lecture)
        else:
            temp[-1] += lecture
    return count <= m


n, m = map(int, input().split())
lectures = list(map(int, input().split()))
print(solution(n, m, lectures))
