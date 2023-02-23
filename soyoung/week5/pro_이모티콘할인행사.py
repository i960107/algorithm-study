from itertools import product

def solution(users, emoticons):
    ans = 0
    result = []
    for sales in list(product([10, 20, 30, 40], repeat=len(emoticons))):
        cnt = 0
        earn = 0
        for user in users:
            money = 0
            for i in range(len(sales)):
                # 할인율이 user의 비율보다 크다면 -> 지불하는 돈
                if sales[i] >= user[0]:
                    money += emoticons[i] * (100 - sales[i]) // 100
            if money >= user[1]:
                cnt += 1
            else:
                earn += money

        if cnt >= ans:
            ans = cnt
            result.append([cnt, earn])
    result.sort(reverse=True)
    return result[0]
