from typing import List
from collections import defaultdict
from itertools import combinations


def solution(info: List[str], query: List[str]) -> List[int]:
    counter = defaultdict(lambda: defaultdict(int))

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
                counter[result][score] += 1

    answer = []

    for q in query:
        temp = q.split(" and ")
        food, min_score = temp[3].split()
        condition = ''.join(temp[:3] + [food])
        min_score = int(min_score)
        total = 0
        for score, count in counter[condition].items():
            if score >= min_score:
                total += count
        answer.append(total)

    return answer
