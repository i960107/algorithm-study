def solution_fail(board):
    answer = 0
    dr = (0,0, 1, -1)
    dc = (1, -1, 0, 0)
    adj = {
        0: [(2, 600), (3, 600), (0, 100)],
        1: [(2, 600), (3, 600), (1, 100)],
        2: [(1, 600), (0, 600), (2, 100)],
        3: [(1, 600), (0, 600), (3, 100)]
    }
    def dfs(r, c, d, cost, visited):
        nonlocal n, min_cost, board
        if r == n - 1 and c == n - 1:
            min_cost = min(min_cost, cost)
            return
       	visited[r][c] = True
        for nxt_d, nxt_cost in adj[d]:
            nr, nc = r + dr[nxt_d], c + dc[nxt_d]
            if not(0 <= nr < n and 0 <= nc < n):
                continue
            if visited[nr][nc] or board[nr][nc] == 1:
                continue
            if cost + nxt_cost >= min_cost:
                continue
            dfs(nr, nc, nxt_d, cost + nxt_cost, visited)
       	visited[r][c] = False
    
    n = len(board)
    min_cost = int(1e9)
    visited = [[False] * n for _ in range(n)]
    # d 는 현재칸에 도착하기 위한 이동 방향 이동하는 방향
    # c는 현재 칸에 도착하기 까지의 비용
    # 현재 칸에는 도로 건설 되지 않음
    dfs(0, 0, 0, 0, visited)
    dfs(0, 0, 2, 0, visited)
    return min_cost
