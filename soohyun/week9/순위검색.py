from typing import List
from collections import defaultdict
from itertools import combinations
from bisect import bisect_right, bisect_left


def solution(info: List[str], query: List[str]) -> List[int]:
    counter = defaultdict(list)

    def replace_condition_with_blank(condition: List[str], indicies: List[int]) -> str:
        for index in indices:
            condition[index] = "-"

        return ''.join(condition)

    for person in info:
        *conditions, score = person.split()
        score = int(score)
        for k in range(5):
            for indices in combinations(range(4), k):
                result = replace_condition_with_blank(conditions[::], indices)
                counter[result].append(score)

    for _, scores in counter.items():
        scores.sort()

    answer = []

    for q in query:
        temp = q.split(" and ")
        food, min_score = temp[3].split()
        condition = ''.join(temp[:3] + [food])
        min_score = int(min_score)
        result = bisect_left(counter[condition], min_score)
        # 만약에 min_score이상인 데이터가 없다면? 왜 통과되지 -> result == len(counter[condition])
        answer.append(len(counter[condition]) - result)
        # result = _bisect_left(counter[condition], min_score)
        # answer.append(len(counter[condition]) - result if result != -1 else 0)
    return answer


def _bisect_left(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] >= target:
            result = mid
            right = mid - 1
    return result


print(_bisect_left([0, 1, 2, 2, 4], -1))
print(_bisect_left([0, 1, 2, 2, 4], 0))
print(_bisect_left([0, 1, 2, 2, 4], 1))
print(_bisect_left([0, 1, 2, 2, 4], 2))
print(_bisect_left([0, 1, 2, 2, 4], 3))
print(_bisect_left([0, 1, 2, 2, 4], 5))
print()

print(bisect_left([0, 1, 2, 2, 4], -1))
print(bisect_left([0, 1, 2, 2, 4], 0))
print(bisect_left([0, 1, 2, 2, 4], 1))
print(bisect_left([0, 1, 2, 2, 4], 2))
print(bisect_left([0, 1, 2, 2, 4], 3))
print(bisect_left([0, 1, 2, 2, 4], 5))
