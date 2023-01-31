def solution(n, l, r):
    answer = 0
    lost = sorted(l)
    reserve = sorted(r)

    for r in reserve[:]:
        if r in lost:
            reserve.remove(r)
            lost.remove(r)

    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)

    answer = n - len(lost)

    return answer
