from typing import List


# 복잡도? 진법 변환한 길이가 N,  O(N)
# 변수 n, number, num 주의! 비슷한 변수 잘못쓰는 실수 많음
# 소수 => 제곱근까지만 체크하면 됨!
def solution(n: int, k: int) -> int:
    primes = set()

    def make_number(arr: List[int]) -> int:
        number = 0
        for i in range(len(arr) - 1, -1, -1):
            number += (arr[i] * (10 ** (len(arr) - i - 1)))
        return number
        # return int(''.join(str(x) for x in arr) if arr else 0)

    def is_prime_number(number: int) -> bool:
        if number < 2:
            return False
        if number in primes:
            return True
        # 소수판별시 2 ~ n의 제곱근까지만 판별해도 소수 판별이 가능
        # 숫자 한개에 대해서 소수인지 판별하는 경우
        # vs 다량의 소수를 한꺼번에 판별해야하는 경우, 소인수분해하는 경우
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                return False
        primes.add(number)
        return True

    result = []
    while n != 0:
        result.append(n % k)
        n = n // k

    temp = []
    count = 0

    for i in range(len(result) - 1, -1, -1):
        if result[i] != 0:
            temp.append(result[i])
        else:
            number = make_number(temp)
            if is_prime_number(number):
                count += 1
            temp = []

    # temp에 남아있는 것을 체크
    if temp:
        number = make_number(temp)
        if is_prime_number(number):
            count += 1
    return count


# print(solution(437674, 3))
# print(solution(1, 3))
print(solution(13, 3))
