import copy
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
result = 0

def bfs():

    queue = deque() # 바이러스가 들어있는 큐
    test_graph = copy.deepcopy(graph)  # bfs()가 호출될 때마다 새로운 test_graph 만들어줌 (깊은 복사: 새로운 메모리 공간에 복사)
    for i in range(n):
        for j in range(m):
            if test_graph[i][j] == 2:
                queue.append([i, j])

    while queue:
        x, y = queue.popleft()
        for dx, dy in d:
            if 0 <= x + dx < n and 0 <= y + dy < m:
                if test_graph[x + dx][y + dy] == 0:
                    test_graph[x + dx][y + dy] = 2
                    queue.append([x + dx, y + dy])

    global result
    cnt = 0
    for i in range(n):
        for j in range(m):
            if test_graph[i][j] == 0:
                cnt += 1

    if result < cnt:
        result = cnt

def make_wall(cnt): # 벽을 itertools
    if cnt == 3:
        bfs()
        return  # 여기 리턴을 빼먹었음! 재귀가 종료되어야 다음 것이 실행 안되고 호출해 준 함수 다음 칸으로 다시 돌아갈 수 있음
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt + 1)
                graph[i][j] = 0  # 재귀 끝나고 돌아오면서 원래 호출한 cnt로 하나씩 차감되고 비로소 0이됨 & graph 값 0으로 다 바꿈

make_wall(0)
print(result)
