from typing import List
from collections import defaultdict
from bisect import bisect_left


def solution(words: List[str], queries: List[str]):
    answer = []

    # xxx??(접미사 와일드카드) -> 앞글자부터 탐색
    dictionary = defaultdict(list)
    # ??xxx(접두사 와일드카드) -> 뒤글자부터 탐색
    reverse_dictionary = defaultdict(list)

    # 글자수별로 그룹화
    for word in words:
        dictionary[len(word)].append(word)
        reverse_dictionary[len(word)].append(word[::-1])

    # 검색 효율성 높이는게 최대 관건. -> 순위 검색 처럼 이진 탐색
    # 이진 검색을 위해 정렬
    for value in dictionary.values():
        value.sort()

    for value in reverse_dictionary.values():
        value.sort()

    def find_range(arr: List[str], target):
        # 모두 와일드카드 였을 경우 -> 모든 글자가 해당
        if target == "":
            return [0, len(arr)]

        left = bisect_left(arr, target)
        # wildcard는 하나 이상이므로 무조건 value들보다 길이 짧음.
        # 조건에 해당하는 문자들 중 맨 앞 인덱스 반환.
        if left >= len(arr) or arr[left][:len(target)] != target:
            return [-1, -1]

        # 조건에 해당하는 마지막 글자보다도 항상 뒤에 있음
        # print(sorted(["fro", "froz", "frs", "frozzzz"]))
        # ['fro', 'froz', 'frozzzz', 'frs']
        # 만약 fro??를 검색한다면 froxx부터  frozzz까지 검색하면 됨.
        # 조건에 해당하는 문자들 중 가장 마지막 인덱스 + 1
        after = target + "z" * len(target)
        right = bisect_left(arr, after)
        return [left, right]

    for query in queries:
        # 와일드 카드 없앰
        wildcard_removed = query.replace("?", "")
        count = 0

        # 접두사 와일드카드
        if query[0] == "?":
            # ????o인 경우 5글자인 단어중 o로 시작하는 단어, ozzzzz로 시작하는 단어
            left, right = find_range(reverse_dictionary[len(query)], wildcard_removed[::-1])

        # 접미사 와일드카드
        else:
            left, right = find_range(dictionary[len(query)], wildcard_removed)

        answer.append(right - left)
    return answer
