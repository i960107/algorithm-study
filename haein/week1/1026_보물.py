N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = sorted(A)
b = sorted(B, key=lambda x: (-x))
num = 0

for i in range(N):
    num += a[i] * b[i]

print(num)
