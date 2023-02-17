from collections import deque
n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()
queue = deque(num)
answer = 0

tmp = 0
for i in range(n):
    if i == 0:
        tmp = queue.popleft()
        answer += tmp
    elif i == n-1:
        tmp = queue.popleft()
        answer += tmp
    else:
        n = queue.popleft()
        answer += (tmp + n)
        tmp = n

print(answer)

'''
push하면 자동으로 정렬이 되고 (즉 push할 때마다 정렬해줘야 할 때)
pop 했을 때 항상 최솟값만 나오게 하려면..
heapq 우선순위큐를 사용하면 된다!!
'''
