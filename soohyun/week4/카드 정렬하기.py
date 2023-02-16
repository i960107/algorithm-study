from typing import List
from sys import stdin
import heapq


def solution_fail(n: int, cards: List[int]) -> int:
    # 가장 작은 수부터 더해가는게 틀린 이유
    # 20, 30, 35, 40, 45
    cards.sort()
    stack = []
    answer = 0
    for card in cards:
        if stack:
            count = stack.pop() + card
            stack.append(count)
            answer += count
        else:
            stack.append(card)
    return answer


def solution(n: int, cards: List[int]) -> int:
    heapq.heapify(cards)
    count = 0
    while len(cards) > 1:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        count += (a + b)
        heapq.heappush(cards, a + b)

    return count


n = int(input())
read = stdin.readline
cards = []

for _ in range(n):
    cards.append(int(read()))
print(solution(n, cards))
