import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
start, end = max(arr), sum(arr)
ans = 0
while start <= end:
    # mid는 최대 블루레이의 크기
    mid = (start + end) // 2
    cnt, part_sum = 1, 0
    for i in arr:
        if part_sum + i <= mid:
            part_sum += i
        else:
            cnt += 1
            part_sum = i
    if cnt > M:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1
print(ans)