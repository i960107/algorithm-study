from typing import List


# 브루트 포스 복잡도 O(N!): 100000! 시간 초과
# 정렬 O(NLogN)
# 어려운 포인트 -> 3, 30, 34중에 어떤 걸 택할 것인가.
#  4, 3, 40, 42이 있을때 43을 선택하는 것이 좋은 전략.
#  4, 1, 40, 42이 있을때 42를 선택하는 것이 좋은 전략.
# 그 수가 가장 우선순위가 높다고 했을때 뒤에 올 수 있는 최대 수
# 42, 423중에 어떤게 더 우선순위가 높은가
def solution(numbers: List[int]) -> str:
    # 총자리수
    # 처음에는 총 자리수만큼 해줘야 한다고 생각. 숫자가 최대 4자리 수임.
    numbers.sort(key=lambda number: str(number) * 4, reverse=True)
    # 정렬 결과에서 제일 먼저 0이 오는 경우 -> 모든 원소가 0
    if numbers[0] == 0:
        return '0'
    return ''.join(map(str, numbers))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
