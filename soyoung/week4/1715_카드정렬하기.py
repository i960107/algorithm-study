import sys
from heapq import *

N = int(sys.stdin.readline())
nums = sorted([int(sys.stdin.readline()) for _ in range(N)])
heapify(nums)
result = []
for _ in range(N-1):
    nx = heappop(nums) + heappop(nums)
    heappush(nums, nx)
    result.append(nx)

print(sum(result))



