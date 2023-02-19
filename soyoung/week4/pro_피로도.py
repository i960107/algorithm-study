from itertools import permutations
def solution(k, dungeons):
    n = len(dungeons)
    ls = list(permutations(dungeons, n))
    ans = 0
    for case in ls:
        hp = k
        cnt = 0
        for a,b in case:
            if hp >= a:
                hp -= b
                cnt += 1
        ans = max(ans, cnt)
    return ans


