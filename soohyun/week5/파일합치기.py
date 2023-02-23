from typing import List
import heapq


# 카드 정렬하기랑 같은 문제 아닌가? 순서가 연속되어야 함.
# 왜 다르지? 왜 826아니고 864
def solution_greedy(k: int, files: List[int]) -> int:
    heapq.heapify(files)
    expense = 0
    while len(files) > 1:
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        expense += (a + b)
        heapq.heappush(files, (a + b))
    return expense


def solution_dp(k: int, files: List[int]) -> int:
    pass


t = int(input())
for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    print(solution_greedy(k, files))
