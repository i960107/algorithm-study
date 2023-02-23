n = int(input())
fibo = [0 for _ in range(n+1)]
fibo[0], fibo[1] = 0, 1

def fibonacci(num):
    if num == 0:
        return fibo[0]
    elif num == 1:
        return fibo[1]

    if fibo[num] == 0:
        fibo[num] = fibonacci(num-1) + fibonacci(num-2)
        return fibo[num]  # 재귀에서 맞물려서 계속 값이 필요할 땐 return 해주는 값이 항상 필요하다!!!
    else:
        return fibo[num]

print(fibonacci(n))
