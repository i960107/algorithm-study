from itertools import permutations
def solution(k, dungeons):
    n = len(dungeons)
    ls = list(permutations(dungeons, n))
    ans = 0
    for case in ls:
        hp = k
        cnt = 0
        for a,b in case:
            if hp >= a:
                hp -= b
                cnt += 1
        ans = max(ans, cnt)
    return ans

# DFS로 풀이
answer = 0
N = 0
visited = []

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0

def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer

