from typing import List
from collections import defaultdict


def solution(want: List[str], number: List[int], discount: List[str]):
    required = defaultdict(int)
    missing = len(want)
    for item, count in zip(want, number):
        required[item] = count

    count = 0
    for day, item in enumerate(discount):
        removed = None

        if day >= 10:
            removed = discount[day - 10]
            required[removed] += 1
            if required[removed] == 1:
                missing += 1

        required[item] -= 1
        if required[item] == 0:
            missing -= 1

        # print(day, item, removed, missing, required.items())
        if missing == 0:
            count += 1

    return count
