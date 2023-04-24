from typing import List
import heapq


def solution_fail(n: int, k: int, enemy: List[int]) -> int:
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


def solution(n: int, k: int, enemy: List[int]) -> int:
    rounds = len(enemy)

    if rounds <= k:
        return rounds

    # 무적권을 사용해서 막을 round들의 enemy. enemy수가 많은 상위 k개르 관리하는 우선순위 큐
    min_heap = []
    # 병사를 사용해서 막은 enemy수
    required = 0
    for r, enemies in enumerate(enemy, 1):
        heapq.heappush(min_heap, enemies)
        # 만약 우선순위 큐의 크기보다 무적권의 개수가 작다면, 가장 작은 enemy는 병사를 사용해 막아야함
        if len(min_heap) > k:
            popped = heapq.heappop(min_heap)
            required += popped
        # 필요한 병사 수가 실제 병사 수보다 크다면 이전 라운드까지만 통과 가능
        if required > n:
            return r - 1

    # 모든 라운드를 통과 가능한 경우
    return rounds
