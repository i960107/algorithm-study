n = int(input())

def fibonacci(num, f):
    if num == 0 or num == 1 or num == 2 or num == 3:
        return f[num]

    if f[num] == 0:
        f[num] = fibonacci(num-1, f) + fibonacci(num-2, f) + fibonacci(num-3, f)
        return f[num]
    else:
        return f[num]

def sol(p, f):
    print(fibonacci(p, f))

for _ in range(n):
    num = int(input())
    f = [0 for _ in range(num + 1)]  # 그냥 애초에 전역 리스트 dp = [0 for _ in range(11)]을 두고 시작하자! -> dp 리스트 재활용 가능!
    if len(f) == 2:
        f[1] = 1
    elif len(f) <= 3:
        f[1] = 1
        f[2] = 2
    elif len(f) >= 4:
        f[1] = 1
        f[2] = 2
        f[3] = 4

    sol(num, f)
