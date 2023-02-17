from heapq import heappush, heappop, heapify
import sys

n = int(input())
arr = list(int(sys.stdin.readline()) for _ in range(n))
heapify(arr)  # arr 자체가 heapq가 되어 정렬 됨

answer = 0
while True:
    if len(arr) == 1:
        break

    a, b = heappop(arr), heappop(arr)
    answer += a+b  # 실수 했던 부분
    heappush(arr, a+b)

print(answer)

