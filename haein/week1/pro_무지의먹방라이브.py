from heapq import heappush, heappop


def solution(food_times, k):
    if k >= sum(food_times):
        return -1

    # 남은 음식 개수
    rest = len(food_times)
    # 이전 음식 시간
    previous = 0

    h = []
    for i in range(len(food_times)):
        heappush(h, (food_times[i], i + 1))

    while k >= 0:
        now = heappop(h)  # 음식 먹는 시간, 음식 번호
        total = (now[0] - previous) * rest

        print(k)
        print(now)
        print(h)
        print("-------")

        if k - total > 0:
            k -= total
            previous = now[0]
            rest -= 1
        else:
            heappush(h, now)
            tmp = sorted(h, key=lambda x: (x[1]))
            return tmp[k % rest][1]


# print(solution([3, 1, 2], 5))

print(solution([3, 5, 1, 6, 5, 3], 20))
