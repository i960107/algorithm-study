def solution(n, times):
    start, end = min(times), max(times)*n
    ans = 0
    while start <= end:
        # mid는 모든 사람이 심사를 받는데 걸리는 최소 시간
        mid = (start + end) // 2
        ppl = 0
        for i in times:
            ppl += (mid // i)
        if ppl < n:
            start = mid + 1
        else:
            ans = mid
            end = mid - 1
    return ans