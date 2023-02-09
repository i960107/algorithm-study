def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    def dfs(v):
        stack = [v]

        while stack:
            value = stack.pop()

            if not visited[value]:
                visited[value] = True
                for k in range(n):
                    if computers[value][k] == 1:
                        stack.append(k)

    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)

    return answer
