import sys

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

sorted_arr = sorted(arr, key=lambda x: (-x[1], -x[0]))

stk = [sorted_arr.pop()]

while len(sorted_arr) > 0:
    n, m = sorted_arr.pop()

    if n >= stk[-1][1]:
        stk.append([n, m])

print(len(stk))

"""
edge case
12
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
7 7

[[12, 14], [2, 13], [8, 12], [8, 11], [6, 10], [5, 9], [3, 8], [5, 7], [7, 7], [0, 6], [3, 5], [1, 4]]

그냥 뒤에 꺼만 내림차순으로 정렬하면 시작시간과 종료시간이 같은 케이스를 커버 불가
스택 자료구조로 뒤에서부터 팝을 해주므로 
[[12, 14], [2, 13], [8, 12], [8, 11], [6, 10], [5, 9], [3, 8], [7, 7], [5, 7], [0, 6], [3, 5], [1, 4]]
이렇게 정렬되게 하려면 만약 뒤의 숫자가 동일해도 앞의 숫자를 기준으로 내림차순 정렬해주어야 함
"""

