# 틀린 풀이
import sys

n = int(input())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n-1):
    p, s, w = map(int, sys.stdin.readline().split())
    graph[p][s] = w
    graph[s][p] = w # 트리는 무방향 그래프이므로

def big_leaf(start_v):
    stack = [start_v]
    tmp = 0
    comp = -1
    node = 0
    while stack:
        p = stack.pop()
        is_root = True
        for j in range(1, n+1):
            print(graph[p][j])
            if graph[p][j] != 0 and j != p:  # 0이면 연결 안 되어 있는 것
                is_root = False
                stack.append(j)  # 갱신된 시작 노드
                tmp += graph[p][j]  # 가중치 -> 이렇게 더하면 이웃한 것끼리 더하게 됨 -> 별도의 그래프 생성해서 visited + 가중치 표현해야
        if is_root: # stack 이용 시, 재귀 이용 시 만약 더이상 갈 곳 없으면 stack 맨 위 pop 하거나 그 전 호출 단계로 알아서 돌아감 (해줄 필요 x)
            if comp < tmp:
                comp = tmp
                node = p
            tmp = 0
    return node

leaf_node = big_leaf(1)
print(leaf_node)

