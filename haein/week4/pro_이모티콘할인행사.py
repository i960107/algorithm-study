# [이모티콘 플러스 가입자, 판매액] -> 최대로
# ([가입자, 판매액]) arr.sorted(arr, key = lambda x: (x[0], x[1]))
# 할인율 10%, 20%, 30%, 40% 중 하나로 설정
# 이모티콘 정렬?
from itertools import product

def solution(users, emoticons):
    answer = []
    discount = [0.9, 0.8, 0.7, 0.6]
    n = len(emoticons)
    result = []

    for i in product(discount, repeat = n): # [0.9, 0.8, 0.7, 0.6]
        new_emoticons = [] # [1170.0, 1170.0, 1170.0, 1170.0]
        people, sales = 0, 0
        sales_pro = [] # [0.9, 0.8, 0.7, 0.6]

        for k in range(n):
            new_emoticons.append(i[k] * emoticons[k])
            sales_pro.append(i[k])
        tmp_total = sum(new_emoticons)

        for per, total in users:
            buy_total = 0
            for p in range(len(sales_pro)): # 이상 할인하는 이모티콘 구매
                if (1-sales_pro[p]) * 100 >= per:
                    # print(buy_total, sales_pro[p], per)
                    buy_total += new_emoticons[p]
                if buy_total >= total: # 플러스 가입
                    people += 1
                    break
            else:
                sales += buy_total

        # print(tmp_total, new_emoticons, sales_pro, people, sales)
        result.append([people, sales])

    result.sort(key = lambda x : (-x[0], -x[1]))

    answer = result[0]

    return answer
