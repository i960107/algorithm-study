# from collections import deque
#
#
# def bfs(start_v):
#     queue = deque()
#     queue.append(start_v)
#     cnt = 1
#     visited = [False for _ in range(n + 1)]
#     visited[start_v] = True
#
#     while queue:
#         v = queue.popleft()
#
#         for i in graph[v]:
#             if not visited[i]:
#                 cnt += 1
#                 queue.append(i)
#                 visited[i] = True
#     return cnt
#
#
# def bfs(start_v):
#     queue = deque()
#     queue.append(start_v)
#     cnt = 0
#     visited = [False for _ in range(n + 1)]
#
#     while queue:
#         v = queue.popleft()
#
#         if visited:
#             continue
#
#         cnt += 1
#         visited[v] = True
#
#         # for i in graph[v]:
#             queue.append(i)
#     return cnt
arr = [0, 0, 0, 0, 0]


def make_wall(cnt):
    if cnt == 3:
        print()
        return  # 여기 리턴을 빼먹었음! 재귀가 종료되어야 다음 것이 실행 안되고 호출해 준 함수 다음 칸으로 다시 돌아갈 수 있음
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt + 1)
                graph[i][j] = 0  # 재
def solution(tickets: List[List[str]]) -> List[str]:
    start = "ICN"

    # 인접 행렬로 만들고

    adj = defaultdict(list)
    for id, (src, dest) in enumerate(tickets):
        adj[src].append((dest, id))

    # 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 하려면
    # 알파벳 순서가 앞서는 경로가 먼저 stack에 추가되어야 함
    for src, dests in adj.items():
        dests.sort()

    # path를 관리해야하나..
    # bfs vs dfs
    # 전체 공항의 수를 어떻게 알 수 있지. 주어진 항공권을 모두 사용해야 함.
    n = len(tickets)

    # visited = set()
    # visited_nodes = []
    # # visited한 공항에 도착했다는 건 전체 공항을 다 한번씩 방문했다는 것? 아님
    # # 전체 공항을 다 체크했는지 어떻게 확인할 수 있지? len(visited)
    # # 재귀로 확인할 수 있는 방법이 있나? -> 반복문으로
    #
    # stack = []
    # stack.append((start, []))
    #
    # while stack:
    #     curr = stack.pop()
    #     visited.add(curr)
    #     visited_nodes.append(curr)
    #
    #     if len(visited) == n + 1:
    #         return visited_nodes
    #
    #     for next in adj[curr]:
    #         if not next in visited:
    #             stack.append(next)

    # 사용한 항공권 id를 관리
    visited = set()
    path = []
    dfs((start, -1), n, adj, visited, path)

    return path


# 방문한 공항 다시 방문할 수도 있음.
# 사용한 항공권 어떻게 처리하지..
def dfs(curr, n: int, adj, visited: Set[str], path: List[str]) -> bool:
    curr, curr_ticket_id = curr

    if curr_ticket_id in visited:
        return False

    visited.add(curr_ticket_id)
    path.append(curr)

    if len(path) == n + 1:
        return True

    for next_info in adj[curr]:
        if next_info[0] not in visited:
            if dfs(next_info, n, adj, visited, path):
                return True

    visited.remove(curr_ticket_id)
    path.pop()

    return False

