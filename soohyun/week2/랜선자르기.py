from typing import List


# parametric search.
def solution(k: int, n: int, cables: List[int]) -> int:
    # lo != 0. [1,1]에서 2개의 케이블을 얻는 경우 zerodivision error발생.
    lo, hi = 1, sum(cables) // n
    max_length = 0
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        cut_cables = get_cut_cable_count(mid, cables)
        if cut_cables >= n:
            max_length = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return max_length


def get_cut_cable_count(l: int, cables: List[int]) -> int:
    return sum([x // l for x in cables])


k, n = map(int, input().split())
cables = []
for _ in range(k):
    cables.append(int(input()))
print(solution(k, n, cables))
