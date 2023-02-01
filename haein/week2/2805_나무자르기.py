n, m = map(int, input().split())
tree = list(map(int, input().split()))


def binary_search(target, data):
    data.sort()
    start = 0
    end = data[-1]

    while start <= end:
        mid = (start + end) // 2
        answer = 0
        for i in data:
            if i > mid:
                answer += i - mid

        if answer >= target:
            # target보다 더 많이 잘려서 절단기가 더 길어져야 하는 상황
            start = mid + 1
        else:
            end = mid - 1

    return end


ans = binary_search(m, tree)
print(ans)
