import sys

n = int(sys.stdin.readline())
num = 0
fibo = []
for i in range(n+1):
    if i == 0:
        num = 0
    elif i <= 2:
        num = 1
    else:
        num = fibo[-1] + fibo[-2]
    fibo.append(num)
print(fibo[-1])