# 런타임 에러
import sys
from collections import deque
N = int(sys.stdin.readline())
dq = deque()
dq.append([N])
ans = []
while dq:
    a = dq.popleft()    # a는 수를 순차적으로 담은 list
    x = a[0]
    if x == 1:
        ans = a
        break
    if x % 2 == 0:
        dq.append([x//2] + a)
    if x % 3 == 0:
        dq.append([x//3] + a)
    dq.append([x-1] + a)
print(len(ans)-1)
print(*ans[::-1])
