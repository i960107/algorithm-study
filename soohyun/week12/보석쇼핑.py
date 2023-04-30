from typing import List
from collections import defaultdict, Counter


# 시간 초과 안 발생하는 이유?
def solution(gems: List[str]) -> List[int]:
    gems_count = len(set(gems))
    current_counter = Counter()

    INF = int(1e9)
    start = end = INF
    left = 0
    # left = right일 수 있음
    # 100000 * 100000 아닌가?
    for right, gem in enumerate(gems):
        current_counter[gem] += 1
        if len([gem for gem, count in current_counter.items() if count >=1]) == gems_count:
            while left < right and current_counter[gems[left]] > 1:
                current_counter[gems[left]] -= 1
                left += 1

            # 어떻게 start가 더 작은 값을 하지?
            # 항상 start <= left?
            if end == INF or end - start > right - left:
                start, end = left, right

            current_counter[gems[left]] -= 1
            left += 1

    return [start + 1, end + 1]


def solution2(gems:List[str]) -> List[int]:
    types = len(set(gems))
    print(types)
    included = defaultdict(int)
    lo, hi = 0, 0
    while hi < len(gems):
        included[gems[hi]] += 1
        if len(included) == types:
            break
        hi += 1
        
    while lo <= hi:
        if included[gems[lo]] == 1:
            break
        included[gems[lo]] -= 1
        lo += 1
        
    final_lo, final_hi = lo, hi
    for _ in range(hi+1, len(gems)):
        hi += 1
        included[gems[hi]] += 1
        while lo < hi:
            if included[gems[lo]] <= 1:
                break
            included[gems[lo]] -= 1
            lo += 1
        if hi - lo < final_hi - final_lo:
            final_lo, final_hi = lo, hi
    return [final_lo +1, final_hi + 1]
        
    

