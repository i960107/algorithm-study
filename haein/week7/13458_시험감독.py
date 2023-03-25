import sys

input = sys.stdin.readline
t = int(input())
stu = list(map(int, input().split()))
a, b = map(int, input().split())
ans = 0

for s in stu:
    if s - a < 0:
        ans += 1
        continue
    else:
        s -= a
        ans += 1
        if s % b > 0: # 나머지가 있으면
            ans += s // b + 1
        else:
            ans += s // b
print(ans)

