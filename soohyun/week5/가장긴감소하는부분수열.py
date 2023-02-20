from typing import List


def solution(n: int, arr: List[int]) -> int:
    # 뒤에서부터 하면 가장 긴 증가 부문 수열
    pass

# 원소가 1000개이기 때문에 brute force로 탐색해서 O(N^2)이어도 가능.
def solution_brute_force(k: int, files: List[int]) -> int:
    for start in range(k):
        part = []
        for end in range(start + 1, k):



# range dp?
def solution_dp(k: int, files: List[int]) -> int:
    # 각 인덱스까지의 가장 긴 감소하는 부분 수열의 길이?
    # 각 인덱스까지의 최소 원소?
    dp = [0] * len(1 + k)
    pass


# 투포인터를 사용할 수 없는 이유. 연속된 원소들만 대상으로 하는게 아님. start - end로 표시할 수 없음
def solution_two_pointer(k: int, files: List[int]) -> int:
    start = 0
    end = 0
    max_desc_len = 0
    for index, file in enumerate(files):
        if files[end] > files[file]:
            end = file
    pass

n = int(input())
arr = list(map(int, input().split()))
print(solution(n, arr))
