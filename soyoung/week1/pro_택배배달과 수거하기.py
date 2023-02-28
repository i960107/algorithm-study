def solution(cap, n, deliveries, pickups):
    # 먼거리부터 탐색하기 위해 두 배열을 뒤집기
    # 가장 먼 집부터 탐색하며 필요한 상자들(배달, 수거)을 갱신 -> d,p에 갱신
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    ans = 0
    d, p = 0, 0
    for i in range(n):
        d += deliveries[i]
        p += pickups[i]
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            ans += (n-i) * 2
    return ans

