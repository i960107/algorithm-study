from typing import List
from itertools import product

from itertools import combinations_with_replacement, permutations


# combinations, permu : 840개, product :256개
# 왜지... 10, 10, 10, 10인 경우도 24개 셈.
def solution(users: List[List[int]], emoticons: List[int]) -> List[int]:
    count = 0
    percent_thresholds = [10, 20, 30, 40]
    # discounts = list(range(max(percent_thresholds), min(percent_thresholds) - 1, -1))
    final = [0, 0]
    for combi in combinations_with_replacement(percent_thresholds, len(emoticons)):
        # 이모티콘 별 할인률, 구입 금액
        # 할인률 : 할인 후 금액
        # set으로 하면 안됨
        for permu in permutations(combi):
            count += 1
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
    print("count:" + str(count))
    return final


# product
def solution2(users: List[List[int]], emoticons: List[int]) -> List[int]:
    discounts = [0.9, 0.8, 0.7, 0.6]
    # discounts = [10, 20, 30, 40]
    # discounts = list(range(max(percent_thresholds), min(percent_thresholds) - 1, -1))
    final = [0, 0]
    count = 0
    for permu in product(discounts, repeat=len(emoticons)):
        new_emoticons = dict()
        count += 1
        for index, (price, dc) in enumerate(zip(emoticons, permu)):
            after_discount = price * dc
            new_emoticons[index] = (dc, after_discount)

        res = [0, 0]
        for percent_threshold, money_threshold in users:
            buy = [price for dc, price in new_emoticons.values() if dc <= (100 - percent_threshold) / 100]
            total_price = int(sum(buy))
            if sum(buy) >= money_threshold:
                res[0] += 1
            else:
                res[1] += total_price
        if res[0] > final[0] or (res[0] == final[0] and res[1] > final[1]):
            final = res
    print("solution2:" + str(count))
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


def solution_haein(users, emoticons):
    answer = []
    discount = [0.9, 0.8, 0.7, 0.6]
    n = len(emoticons)
    result = []

    for i in product(discount, repeat=n):  # [0.9, 0.8, 0.7, 0.6]
        new_emoticons = []  # [1170.0, 1170.0, 1170.0, 1170.0]
        people, sales = 0, 0
        sales_pro = []  # [0.9, 0.8, 0.7, 0.6]

        for k in range(n):
            new_emoticons.append(i[k] * emoticons[k])
            sales_pro.append(int(100 - i[k]*100))
        tmp_total = sum(new_emoticons)

        for per, total in users:
            buy_total = 0
            for p in range(len(sales_pro)):  # 이상 할인하는 이모티콘 구매
                if sales_pro[p] >= per:
                    # print(buy_total, sales_pro[p], per)
                    buy_total += new_emoticons[p]
                if buy_total >= total:  # 플러스 가입
                    people += 1
                    break
            else:
                sales += buy_total

        # print(tmp_total, new_emoticons, sales_pro, people, sales)
        result.append([people, sales])

    result.sort(key=lambda x: (-x[0], -x[1]))

    answer = result[0]

    return answer


# print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
# print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],
#                [1300, 1500, 1600, 4900]))

print(solution_haein([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],
               [1300, 1500, 1600, 4900]))
#
# print(solution2([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],
#                 [1300, 1500, 1600, 4900]))
