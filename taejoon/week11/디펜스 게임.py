import heapq


def solution(n, k, enemy):
    pq = []
    answer = 0

    for en in enemy:
        if n >= en:
            n -= en
            heapq.heappush(pq, -en)
        else:
            if k == 0:
                break
            elif len(pq) == 0 and k > 0:
                k -= 1
            elif -pq[0] > en and k > 0:
                n += -pq[0]
                heapq.heappop(pq)
                n -= en
                heapq.heappush(pq, -en)
                k -= 1
            elif en >= -pq[0] and k > 0:
                k -= 1
        answer += 1

    return answer
