from typing import List


def solution_two_pointer(n: int, values: List[int]) -> List[int]:
    # O(N)
    values.sort()
    left, right = 0, n - 1

    solution1, solution2 = values[left], values[right]
    mixed_solution = abs(solution1 + solution2)

    while left < right:
        curr_mixed = values[left] + values[right]

        if abs(curr_mixed) < mixed_solution:
            solution1, solution2, mixed_solution = values[left], values[right], abs(curr_mixed)
            if mixed_solution == 0:
                break

        if curr_mixed < 0:
            left += 1

        else:
            right -= 1

    return [solution1, solution2]


def solution_binary_search(n: int, solutions: List[int]) -> List[int]:
    # O(N//2logN)
    solutions.sort()
    checked = set()

    answer = []
    mixed = float("inf")

    for index, solution in enumerate(solutions):
        if solution in checked:
            continue
        solution_to_mix = get_solution_to_mix_to_minimize_value(solution, solutions, index + 1)
        if abs(solution + solution_to_mix) < mixed:
            answer = [solution, solution_to_mix]
            mixed = sum(answer)
            if sum(answer) == 0:
                break
        checked.add(solution)
        checked.add(solution_to_mix)

    return answer


def get_solution_to_mix_to_minimize_value(solution: int, solutions: List[int], lo: int = 0) -> int:
    hi = len(solutions) - 1

    # 오른쪽 범위만 탐색하면 됨.
    solution_to_mix = -1
    min_mixed = float('inf')

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        mixed = solution + solutions[mid]

        if abs(mixed) < abs(min_mixed):
            solution_to_mix = solutions[mid]
            min_mixed = mixed

            if mixed == 0:
                return mid

        if mixed < 0:
            lo = mid + 1

        else:
            hi = mid - 1

    return solution_to_mix


n = int(input())
# 모두 다른 값(중복 없음), 정렬되어 있지 않음
values = list(map(int, input().split()))
print(*solution_binary_search(n, values))
