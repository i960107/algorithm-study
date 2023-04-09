from typing import List
from itertools import combinations
from collections import defaultdict


def solution(orders: List[str], course: List[int]) -> List[str]:
    candidates = defaultdict(int)
    for order in orders:
        menus = list(order)
        menus.sort()
        for count in course:
            for combi in combinations(menus, count):
                candidates[''.join(combi)] += 1

    max_selected = defaultdict(int)
    for combi, count in candidates.items():
        if count < 2:
            continue
        if max_selected[len(combi)] < count:
            max_selected[len(combi)] = count
    print(max_selected.items())

    answer = []
    for combi, count in candidates.items() \
            :
        if count == max_selected[len(combi)]:
            answer.append(combi)
    answer.sort()
    return answer

# 조합 함수 이용하지 않고
def solution2(orders: List[str], course: List[int]) -> List[str]:
    candidates = defaultdict(int)
    for order in orders:
        menus = list(order)
        menus.sort()
        for count in course:
            for combi in combinations(menus, count):
                candidates[''.join(combi)] += 1

    max_selected = defaultdict(int)
    for combi, count in candidates.items():
        if count < 2:
            continue
        if max_selected[len(combi)] < count:
            max_selected[len(combi)] = count
    print(max_selected.items())

    answer = []
    for combi, count in candidates.items() \
            :
        if count == max_selected[len(combi)]:
            answer.append(combi)
    answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
