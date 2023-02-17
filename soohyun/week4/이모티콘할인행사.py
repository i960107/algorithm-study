from typing import List
from itertools import combinations_with_replacement, permutations


def solution(users: List[List[int]], emoticons: List[int]) -> List[int]:
    percent_thresholds = [percent for percent, price in users]
    # discounts = list(range(max(percent_thresholds), min(percent_thresholds) - 1, -1))
    final = [0, 0]
    for combi in combinations_with_replacement(percent_thresholds, len(emoticons)):
        # 이모티콘 별 할인률, 구입 금액
        # 할인률 : 할인 후 금액
        # set으로 하면 안됨
        for permu in permutations(combi):
            after_dc_emoticons = dict()
            for index, (price, dc) in enumerate(zip(emoticons, permu)):
                after_dc = price * (100 - dc) / 100
                after_dc_emoticons[index] = (dc, after_dc)

            res = [0, 0]
            for percent_threshold, money_threshold in users:
                buy = [price for dc, price in after_dc_emoticons.values() if dc >= percent_threshold]
                total_price = int(sum(buy))
                if sum(buy) >= money_threshold:
                    res[0] += 1
                else:
                    res[1] += total_price
            if res[0] > final[0] or (res[0] == final[0] and res[1] > final[1]):
                final = res
    return final


def solution_fail(users: List[List[int]], emoticons: List[int]) -> List[int]:
    final = [0, 0]
    best_strategy = []
    for price in emoticons:
        best_strategy.append(get_best_discount_ratio(users, price))

    print(best_strategy)
    return final


# 각 이모티콘별로, 판매금액이 가장 높은 discount를 선택한다?아님.
# user별로 판매량이 높아야함.
# 할인율이 낮을수록 구입하는 사람수는 적지만, 한 사람당 구입 금액이 높아짐.
def get_best_discount_ratio(users: List[List[int]], price):
    percent_thresholds = [percent for percent, price in users]
    discounts = list(range(max(percent_thresholds), min(percent_thresholds) - 1, -1))

    final_total_sales, final_discount_ratio = 0, 0
    for discount in discounts:
        total_sales = sum([price * (100 - discount) / 100 for discount_threshold, price_threshold in users if
                           discount_threshold <= discount])
        if final_total_sales < total_sales:
            final_total_sales, final_discount_ratio = total_sales, discount

    return [final_total_sales, final_discount_ratio]


# print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],
               [1300, 1500, 1600, 4900]))
