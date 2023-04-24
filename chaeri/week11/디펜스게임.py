from heapq import heappop, heappush

def solution(n, k, enemy):
    heap = []
    answer, total = 0, 0
    for each in enemy:
        heappush(heap, -each)
        total += each
        if total > n:
            if k == 0: 
                break
            total += heappop(heap) 
            k -= 1
        answer += 1
    return answer