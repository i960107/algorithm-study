# itertools combinations 를 사용해 풀었으나 시간 초과
# 투 포인터를 사용해서 풀어보려 했으나 0과 가장 가까운 것을 구하는 과정에서 어려웠음
# 참고해서 풀음
import sys

n = int(input())
liq = list(map(int, sys.stdin.readline().split()))
liq.sort()


def two_pointers(data):
    start = 0
    end = len(data) - 1
    comp = 2000000001
    tmp = []

    while start < end:
        interval_sum = data[start] + data[end]

        if abs(interval_sum) < comp:
            tmp = [data[start], data[end]]
            comp = abs(interval_sum)

        if interval_sum < 0:  # 단순하게 생각해서 합이 0보다 작으면 0에 가까워지려면 수가 더 커져야 함 -> start += 1
            start += 1
        else:  # 합이 0보다 크면 0에 가까워지려면 수가 더 작아져야 함 -> end -= 1
            end -= 1
    return tmp


a, b = two_pointers(liq)
print(a, b)
