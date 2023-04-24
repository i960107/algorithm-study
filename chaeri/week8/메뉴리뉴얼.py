from itertools import combinations

def solution(orders, course):
    answer = []
    for course_num in course:
        menu = dict()
        arr = []
        
        #orders의 메뉴 조합 만들기
        for order in orders:
            s_order = sorted(order)
            arr.extend(list(combinations(s_order, course_num)))

        #dict로 횟수 카운트
        for a in arr:
            key = ''.join(a)
            if key in menu:
                menu[key] += 1
            else:
                menu[key] = 1
        
        #한 번 이상 주문된 것들 찾기
        for i in menu:
            if max(menu.values()) > 1:
                if menu[i] == max(menu.values()):
                    answer.append(i)

    answer.sort()
    return answer