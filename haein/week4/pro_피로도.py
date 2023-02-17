from itertools import permutations

def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    started_k = k
    dun = list(permutations(dungeons, n))
    result, tmp = 0, 0

    for i in dun: # ([80, 20], [50, 40], [30, 10])
        if result < tmp:
            result = tmp
        tmp, k = 0, started_k

        for j in range(len(i)):
            a, b = i[j][0], i[j][1]
            if k >= a:
                k -= b
                tmp += 1
            else:
                break

    answer = result

    return answer
