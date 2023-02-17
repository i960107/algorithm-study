# O(N^2). 압축 단위(1 ~ N//2)에 대해서 전체 문자열 확인. 1000 * 1000 = 1,000,000 괜찮은 방법.
def solution(s: str) -> int:
    min_length = len(s)
    for unit in range(1, len(s) // 2 + 1):
        res = compress(unit, s)
        print(res)
        min_length = min(min_length, len(res))
    return min_length


def compress(unit: int, s: str) -> str:
    compressed = []
    prev = ""
    repeated = 0
    for start in range(0, len(s), unit):
        curr = s[start:start + unit]
        if curr == prev:
            repeated += 1
        else:
            compressed.extend((repeated, prev))
            prev = curr
            repeated = 1

    compressed.extend((repeated, prev))
    return ''.join([str(x) for x in compressed if x not in (0, 1)])


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
