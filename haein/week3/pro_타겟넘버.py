# sol 1.
# 재귀 풀이
def solution(numbers, target):
    cnt = 0
    def dfs(index, tmp):
        nonlocal cnt
        index += 1

        if index == len(numbers):
            if tmp == target:
                cnt += 1
            return

        dfs(index, tmp + numbers[index])
        dfs(index, tmp - numbers[index])

    dfs(-1, 0)

    return cnt

# sol 2.
# BFS 풀이

from collections import deque
def solution(numbers, target):
    answer = 0

    def bfs():
        nonlocal answer
        queue = deque()
        queue.append((0, numbers[0]))
        queue.append((0, -numbers[0]))

        while queue:
            idx, result = queue.popleft()

            if idx < len(numbers) - 1:
                queue.append((idx + 1, result + numbers[idx + 1]))
                queue.append((idx + 1, result - numbers[idx + 1]))
            else:
                # idx가 len(numbers) - 1 이상일 땐 더이상 idx + 1 안 함
                # idx가 max에 달한 것 중 그 결과값만 보는 것!
                # deque엔 idx가 max에 달한 것과 끝까지 계산 시 그 결과값들이 들어있음.
                # 하나씩 queue에서 꺼내서 queue가 없어질 때까지 result == target인지 보는 것
                if result == target:
                    answer += 1
    bfs()

    return answer

# sol 3.
# DFS 풀이
def solution(numbers, target):
    answer = 0

    def dfs():
        nonlocal answer
        stack = [[0, numbers[0]], [0, -numbers[0]]]

        while stack:
            idx, result = stack.pop()

            if idx <= len(numbers) - 2:
                stack.append([idx + 1, result + numbers[idx + 1]])
                stack.append([idx + 1, result - numbers[idx + 1]])
            else:
                if result == target:
                    answer += 1

    dfs()

    return answer
