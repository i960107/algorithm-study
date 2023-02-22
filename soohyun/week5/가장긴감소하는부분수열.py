from typing import List


# 원소가 1000개이기 때문에 brute force로 탐색해서 O(N^2)이어도 가능.
# dp를 기록하지 않는다면? 매 end마다 모든 경우의 수를 살펴봐야 함. 이미 살펴본 경우도 포함.
# dp를 기록한다면? 이미 살펴본 경우가 dp에 기록되어 있음. 해당 인덱스의 숫자가 포함된 부분 수열 중 가장 긴 감소하는 수열의 길이의 경우만 살펴보면 됨.
# Linear DP? ragne DP? 어떤 DP에 속하지?
def solution_brute_force(k: int, arr: List[int]) -> int:
    dp = [0] * (k + 1)
    for end in range(k):
        count = 0
        for start in range(k - 1):
            if arr[end] < arr[start]:
                count = max(dp[start + 1], count)
        count += 1
        dp[end + 1] = count
    return max(dp)


# range dp?
def solution_dp(k: int, arr: List[int]) -> int:
    # 각 인덱스까지의 가장 긴 감소하는 부분 수열의 길이?
    # 각 인덱스까지의 최소 원소?
    dp = [0] * (k + 1)
    pass


# 투포인터를 사용할 수 없는 이유. 연속된 원소들만 대상으로 하는게 아님. start - end로 표시할 수 없음
def solution_two_pointer(k: int, arr: List[int]) -> int:
    start = 0
    end = 0
    max_desc_len = 0


n = int(input())
arr = list(map(int, input().split()))
print(solution_brute_force(n, arr))
