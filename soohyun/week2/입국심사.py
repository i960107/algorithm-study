from typing import List


def solution(n: int, officers: List[int]) -> int:
    m = len(officers)
    max_time = max(officers)
    # 최소 시간을 뭘로 잡지..
    # 크게 의미가 없다고 생각 O(LogN)복잡도를 가지므로.
    lo, hi = 0, max_time * n
    answer = None
    while lo <= hi:
        # mid => 모든 사람이 심사를 받는데 걸리는 시간
        mid = lo + (hi - lo) // 2
        if can_all_people_immigrate_in_time(n, mid, officers):
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return answer


def can_all_people_immigrate_in_time(n: int, time: int, officers: List[int]) -> bool:
    immigrated = 0
    for officer in officers:
        immigrated += time // officer
    return immigrated >= n


print(solution(6, [7, 10]))
