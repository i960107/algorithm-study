from typing import List


# dfs, 재귀적으로 풀이
def solution_recursive_dfs(numbers: List[int], target: int) -> int:
    return brute_force(numbers, 0, 0, target)


# index: 이번에 처리할 Index.
# 어떤 값을 반환해야할까. 두가지 값이 있는데.
# 반환값이 있는 경우, 반환값이 없는 경우
# 반환값이 있는 경우 반환값이 두개인데 어떻게 반환해야 하지
# brute_force가 dfs가 되지 않나.
def brute_force(numbers: List[int], index: int, accumulated: int, target: int) -> int:
    if index == len(numbers):
        if accumulated == target:
            return 1
        else:
            return 0

    count = 0

    count += brute_force(numbers, index + 1, accumulated + numbers[index], target)
    count += brute_force(numbers, index + 1, accumulated - numbers[index], target)

    return count


# 인접 그래프랑 다른점 -> 방문해야하는 순서가 정해져 있음. 모든 경우의 수를 확인한다.
def solution_iterative_dfs(numbers: List[int], target: int) -> int:
    # 방문할 index, accumulated
    stack = [(0, 0)]
    count = 0

    while stack:
        index, acc = stack.pop()

        if index == len(numbers):
            if acc == target:
                count += 1
            continue

        stack.append((index + 1, acc + numbers[index]))
        stack.append((index + 1, acc - numbers[index]))

    return count


print(solution_recursive_dfs([1, 1, 1, 1, 1], 3))
print(solution_recursive_dfs([4, 1, 2, 1], 4))

print(solution_iterative_dfs([1, 1, 1, 1, 1], 3))
print(solution_iterative_dfs([4, 1, 2, 1], 4))
