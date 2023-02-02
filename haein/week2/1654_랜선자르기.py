k, n = map(int, input().split())
line = []
for _ in range(k):
    line.append(int(input()))


def binary_search(target, data):
    data.sort()
    start = 1  # 0으로 하면 ZeroDivisionError
    end = data[-1]
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in data:
            cnt += i // mid
        if target <= cnt:  # 적어도 target 개 이상의 랜선을 잘라야 하므로 =를 여기에 붙이는 게 맞음!
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    return answer


ans = binary_search(n, line)
print(ans)
