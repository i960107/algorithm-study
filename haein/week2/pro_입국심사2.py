def solution(n, times):

    start,end = 1, max(times) *n
    res = end
    while start <= end:
        mid = (start + end) // 2

        people = 0
        for time in times:
            people += (mid // time)

        if people < n:
            start = mid+1
        else: #people >= n:
            end = mid-1
            res = min(res, mid)

    return res
