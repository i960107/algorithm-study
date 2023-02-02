def solution(n, times):
    answer = 0
    origin_time = times

    start = 1
    end = max(times) * n
    times.sort()

    while start <= end:
        mid = (start + end) // 2
        # 심사 받은 사람 수
        cnt = 0
        interval_sum = 0
        # 총 심사 받는 데에 걸리는 시간
        for i in range(n):
            interval_sum = min(times)
            times[times.index(min(times))] += origin_time[times.index(min(times))]
            cnt += 1

        if cnt <= n:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer
