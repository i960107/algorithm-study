def solution(l: int, p: int, v: int) -> int:
    return v // p * l + min(l, v % p)


case = 0
while True:
    case += 1
    l, p, v = map(int, input().split())
    if l + p + v == 0:
        break
    print('Case %d: %d' % (case, solution(l, p, v)))
