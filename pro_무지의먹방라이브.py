from collections import deque

# solution 1
def solution(food_times, k):
    dq = deque()
    length = len(food_times)

    for i in range(length):
        dic = dict()
        dic[i + 1] = food_times[i]
        dq.append(dic)

    for i in range(k):
        if len(dq) > 0:
            tmp = dq.popleft()
            if list(tmp.values())[0] - 1 != 0:
                dic = dict()
                dic[list(tmp.keys())[0]] = list(tmp.values())[0] - 1
                dq.append(dic)
        else:
            return -1

    if len(dq) > 0:
        tmp = dq.popleft()
        answer = list(tmp.keys())[0]
    else:
        answer = -1

    return answer

# solution 2

from collections import deque

def solution(food_times, k):
    length = len(food_times)
    order = deque() # 남은 순서만 가지고 있음
    food = deque() # 음식 남은 초만 가지고 있음
    for i in range(length):
        order.append(i+1)
        food.append(food_times[i])

    for i in range(k):
        if len(order) > 0:
            order_tmp = order.popleft()
            food_tmp = food.popleft()
            if food_tmp - 1 != 0:
                food.append(food_tmp-1)
                order.append(order_tmp)
        else:
            return -1

    if len(order) > 0:
        answer = order.popleft()
    else:
        answer = -1

    return answer
