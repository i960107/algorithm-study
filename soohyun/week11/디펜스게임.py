from typing import List
import heapq


def solution_fail(n:int, k:int, enemy:List[int]) -> int:
    n = len(enemy)
    
    if n <= k:
        return n
    
    min_heap = []
    required = 0
    for r, enemies in enumerate(enemy, 1):
        heapq.heappush(min_heap, enemies)
        if len(min_heap) > k:
            popped = heapq.heappop(min_heap)
            required += popped
        if required > n:
            return r - 1
        print(min_heap)

def solution(n:int, k:int, enemy:List[int]) -> int:
    rounds = len(enemy)
    
    if rounds <= k:
        return rounds
    
    min_heap = []
    required = 0
    for r, enemies in enumerate(enemy, 1):
        heapq.heappush(min_heap, enemies)
        if len(min_heap) > k:
            popped = heapq.heappop(min_heap)
            required += popped
        if required > n:
            return r - 1
        
    return rounds 
