from itertools import permutations
def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    print(weak)
    ans = len(dist) + 1
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            cnt = 1
            position = weak[start] + friends[cnt-1]
            for i in range(start, start+length):
                # 친구의 위치 구하기
                if position < weak[i]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    position = weak[i] + friends[cnt-1]
            ans = min(cnt, ans)
    if ans > len(dist):
        return -1
    return ans

