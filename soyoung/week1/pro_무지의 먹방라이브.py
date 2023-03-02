import heapq

def solution(food_times, k):
    ans = -1
    q = []
    food_num = len(food_times)
    for i in range(food_num):
        heapq.heappush(q, (food_times[i], i + 1))
    previous = 0  # 이전에 제거한 음식의 food_time
    while q:
        # 먹는데 걸리는 시간: 남은양 * 남은음식개수
        t = (q[0][0] - previous) * food_num
        if k >= t:
            k -= t
            previous, _ = heapq.heappop(q)
            food_num -= 1
        # 시간이 부족할 경우(음식을 다 못먹을 경우) 남은 음식 중에 먹어야할 음식 찾기
        else:
            idx = k % food_num
            q.sort(key=lambda x: x[1])
            ans = q[idx][1]
            break
    return ans

