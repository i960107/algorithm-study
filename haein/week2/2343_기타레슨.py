n, m = map(int, input().split())
blue = list(map(int, input().split()))


def binary_search(target, data):
    start = max(data)
    end = sum(data)
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        interval_sum = 0
        for i in range(len(data)):
            interval_sum += data[i]
            if interval_sum <= mid and i == 0:
                cnt += 1
            elif i == 0 and interval_sum > mid:
                break
            if interval_sum > mid:
                cnt += 1
                interval_sum = data[i]
            if cnt > target:
                break
        if cnt <= target:  # 블루레이 개수보다 이하이면 더 크게 쪼개진 것이므로 최소 길이를 줄여야 한다
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer


print(binary_search(m, blue))
