# 참고 풀이 https://www.youtube.com/watch?v=yYc2KiCSIoA&t=37s&ab_channel=ezsw

import itertools
import math

def solution(n, weak, dist):
    weakSize = len(weak) # 취약지점 리스트의 인덱스
    weak = weak + [w + n for w in weak]
    minCnt = math.inf

    for start in range(weakSize): # 취약지점 리스트의 출발지점
        for d in itertools.permutations(dist, len(dist)): # 1시간마다 갈 수 있는 거리 리스트 순열
            cnt = 1 # 리스트 1개마다 ( , , ) 일단 시작하는 지점은 취약지점이므로 한 군데 체크! -> 친구 수 체크
            pos = start # 취약지점 현재 인덱스
            for i in range(1, weakSize): # 1 보다 크고 취약지점 인덱스 끝까지
                nextPos = start + i # 취약지점 다음 인덱스
                diff = weak[nextPos] - weak[pos]
                if diff > d[cnt-1]: # 다음 취약지점까지 현재 있는 거리가 안 된다면 다음 친구가 가야 함
                    pos = nextPos
                    cnt += 1

            if cnt <= len(dist):
                minCnt = min(minCnt, cnt)

    if minCnt == math.inf:
        return -1

    return minCnt
