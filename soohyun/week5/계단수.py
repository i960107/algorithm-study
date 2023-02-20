n = int(input())
denominator = 1000000000
dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(n + 1)]
for k in range(1, 10):
    dp[1][k][1 << k] = 1

# 최악의 경우 1024  * 10 * 100 + 1  = 1,024,000번 연산 필요
# range(1, n)이 아닌 이유?
for len in range(n):
    for last in range(10):
        for bit in range(1024):
            if last < 9:
                next_bit = bit | (1 << (last + 1))
                dp[(len + 1)][last + 1][next_bit] += dp[len][last][bit]
                # 매번 나머지 연산 해줘야하나? 안 해줄때와 차이가 큰가?
                # 나눗셈 연산을 중간에 해줘도 결과는 같은가?
                # 12 % 10 = 2,  (2+4)% 10 =6, (12 + 4)% 10 = 6 같음.
                dp[(len + 1)][last + 1][next_bit] %= denominator
            if last > 0:
                next_bit = bit | (1 << (last - 1))
                dp[(len + 1)][last - 1][next_bit] += dp[len][last][bit]
                dp[(len + 1)][last - 1][next_bit] %= denominator

res = 0
# 맨 앞자리에 0이 오는 경우 제외
for last in range(10):
    res += dp[n][last][1023]
    res %= denominator

print(res)
