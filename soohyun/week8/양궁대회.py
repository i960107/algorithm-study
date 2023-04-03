import copy
from typing import List
from itertools import combinations_with_replacement


def solution(n: int, info: List[int]) -> List[int]:
    def get_score_diff(apeach: List[int], lion: List[int]) -> int:
        apeach_score = 0
        lion_score = 0
        for i, (a, l) in enumerate(zip(apeach, lion)):
            if a == l == 0:
                continue
            score = 10 - i
            if a < l:
                lion_score += score
            else:
                apeach_score += score
        return lion_score - apeach_score

    def dfs(lion: List[int], m: int, target: int):
        # m 남은 발 수
        if target == -1:
            # nonlocal answer_info 하지 않으면 에러
            # 참조변수여도 nonlocal지정해주어야 함 아니면 새로운 변수로 선언됨
            nonlocal max_gap, answer
            score_diff = get_score_diff(info, lion)
            # 낮은 점수를 더 많이 맞춘 경우가 더 늦게 나옴? 아닌 듯.
            # score_diff는 0보다 커야함. 최종 점수가 같을 경우 어피치가 우승
            if score_diff <= 0:
                return

            result = copy.deepcopy(lion)
            if score_diff > max_gap:
                max_gap, answer = score_diff, [result]
            if score_diff == max_gap:
                answer.append(result)

            return

        target_score = target
        target_index = 10 - target

        # 0점은 남은 발 다 쏘기
        if target_score == 0:
            lion[target_index] = m
            dfs(lion, 0, -1)
            lion[target_index] = 0
            return

        # 어피치가 맞춘 횟수 +1발을 맞춰서 점수를 얻는 경우
        if info[target_index] < m:
            lion[target_index] = info[target_index] + 1
            dfs(lion, m - info[target_index] - 1, target_score - 1)
            lion[target_index] = 0

        # 0발을 맞추고 어피치가 점수를 따는 경우
        dfs(lion, m, target_score - 1)

    max_gap = 0
    answer = []
    lion = [0] * 11

    dfs(lion, n, 10)

    if not answer:
        return [-1]

    answer.sort(key=lambda x: x[::-1], reverse=True)
    # 에러나는 이유?
    # answer.sort()
    return answer[0]


def solution2(n: int, apeach_info: List[int]) -> List[int]:
    answer = [-1]
    max_gap = 0
    # 낮은 점수를 더 많이 맞추는 경우가 먼저 나옴
    # for combi in combinations_with_replacement(range(0, 11), n):
    for combi in combinations_with_replacement(range(0, 11), n):
        lion_info = [0] * 11
        lion, apeach = 0, 0

        for score in combi:
            lion_info[10 - score] += 1

        for index, (l, a) in enumerate(zip(lion_info, apeach_info)):
            if a == l == 0:
                continue
            if l > a:
                lion += (10 - index)
            else:
                apeach += (10 - index)

        gap = lion - apeach
        # 점수차가 더 높은 경우메나 선택
        if gap > max_gap:
            max_gap, answer = gap, lion_info
    return answer


# print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
# print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))


arr = [[2, 3, 1, 0, 0, 0, 0, 1, 3, 0, 0], [2, 1, 0, 2, 0, 0, 0, 2, 3, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
       [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
arr.sort()
print(arr)
print(arr[0])

arr2 = [[2, 3, 1, 0, 0, 0, 0, 1, 3, 0, 0], [2, 1, 0, 2, 0, 0, 0, 2, 3, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
arr2.sort(key=lambda x: x[::-1], reverse=True)
print(arr2)
print(arr2[0])
