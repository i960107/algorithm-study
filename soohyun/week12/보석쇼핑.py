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
        if len([gem for gem, count in current_counter.items() if count >= 1]) == gems_count:
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


def solution2(gems: List[str]) -> List[int]:
    # 전체 보석 종류
    types = len(set(gems))

    # 윈도우 안에 포함된 보석 종류
    included = defaultdict(int)
    # [lo:hi] 보석 포함
    lo, hi = 0, 0

    # 모든 보석을 포함할때까지 오른쪽 포인터 이동
    while hi < len(gems):
        included[gems[hi]] += 1
        if len(included) == types:
            break
        hi += 1

    # 필수적인 보석만 포함될때까지 left pointer이동 시켜 최소 윈도우 만들기
    while lo <= hi:
        if included[gems[lo]] == 1:
            break
        included[gems[lo]] -= 1
        lo += 1

    final_lo, final_hi = lo, hi
    # 윈도우 이동시키면서 더 작은 윈도우 가능한지 파악.
    for _ in range(hi + 1, len(gems)):
        hi += 1
        included[gems[hi]] += 1
        while lo < hi:
            if included[gems[lo]] <= 1:
                break
            included[gems[lo]] -= 1
            lo += 1
        if hi - lo < final_hi - final_lo:
            final_lo, final_hi = lo, hi
    return [final_lo + 1, final_hi + 1]


# 할인 행상 풀이와 동일
def solution3(gems: List[str]) -> List[int]:
    # 전체 보석 종류
    types = set(gems)

    # 필요한 개수 대비 가지고 있는 보석 수
    required = {t: 1 for t in types}
    # 포함되지 않은 보석 종류
    missing = len(types)

    # [lo:hi] 보석 포함
    # 슬라이딩 윈도우 left, right. 가장 작은 슬라이딩 윈도우 start, end
    left = start = end = 0

    for right, gem in enumerate(gems, 1):
        required[gem] -= 1
        if required[gem] == 0:
            missing -= 1

        if missing == 0:
            while left < right and required[gems[left]] < 0:
                required[gems[left]] += 1
                left += 1

            if not end or right - left < end - start:
                start, end = left, right
                required[gems[left]] += 1
                missing += 1
                left += 1

    return [start + 1, end]


def solution_chaeri(gems):
    answer = []
    short = len(gems)
    start, end = 0, 0
    check = len(set(gems))  # 보석의 총 종류 수
    contained = {}

    while end < len(gems):

        if gems[end] not in contained:  # 보석 발견
            contained[gems[end]] = 1
        else:
            contained[gems[end]] += 1

        end += 1

        if len(contained) == check:  # 현재 구간내 모든 종류가 다 있다면
            while start < end:
                if contained[gems[start]] > 1:  # start에 해당하는 보석이 구간 내에 하나 이상 있을 때
                    contained[gems[start]] -= 1
                    start += 1

                elif not answer or short > end - start:
                    short = end - start
                    answer = [start + 1, end]  # answer와 최단거리 갱신
                    break

                else:
                    break

    return answer


# print(solution_chaeri(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution_chaeri(["A", "B", "C", "D"]))
