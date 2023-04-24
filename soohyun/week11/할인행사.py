from typing import List
from collections import defaultdict


def solution(want: List[str], number: List[int], discount: List[str]):
    # 할인행사는 총 일 수 100,000 * 10 = > 1,000,000으로 brute force시에도 통과는 가능
    # 만약 기준일이 100,000정도이고 효율성 검사 있었다면 sliding window필요

    # 각 아이템별 필요한 개수 대비 실제 개수
    # value > 0 모자라다. value == 0 필요한만큼 있다. value < 0 과하다.
    required = defaultdict(int)
    # 모자란 아이템 종류의 개수
    missing = len(want)
    for item, count in zip(want, number):
        required[item] = count

    count = 0
    for day, item in enumerate(discount):
        if day >= 10:
            removed = discount[day - 10]
            required[removed] += 1
            # value == 1이 되었다는건 필요한 아이템이었다는 것
            # 원래 필요하지 않는 아이템이 장바구니에서 없어지면 최대 값 0
            if required[removed] == 1:
                missing += 1

        required[item] -= 1
        # 아이템을 뺐는데 value == 0이 되었다면, 필요한 아이템이었다는 것
        # 원래 필요하지 않은 아이템이 장바구니에서 없어지면 음수값이 됨.
        if required[item] == 0:
            missing -= 1

        # print(day, item, removed, missing, required.items())
        if missing == 0:
            count += 1

    return count
