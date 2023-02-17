def solution(commands):
    graph = [[[0, ""] for _ in range(51)] for _ in range(51)]
    answer = []
    merge_code = 1
    # 각 셀에 들어가는 것 [merge 여부 (0이면 X, 1부터 merge code), value]

    for c in commands:
        if c[0:6] == 'UPDATE':
            if c[7].isdigit():
                command, r, c, v = c.split()
                graph[r][c] = [0, v]
            else:
                command, v1, v2 = c.split()
                for i in range(1, 51):
                    for j in range(1, 51):
                        if graph[i][j][1] == v1:
                            graph[i][j] = [graph[i][j][0], v2]
        elif c[0:5] == 'MERGE':
            command, r1, c1, r2, c2 = c.split()
            if (r1, c1) == (r2, c2):
                continue
            else:
                move = [(0,1), (1,0), (0, -1), (-1, 0)]
                for my, mx in move:
                    ny, nx = r1 + my, c1 + mx
                    if ny < 1 or ny > 50 or nx < 1 or nx > 50: # 인접 X
                        break
                    else: # 인접 O
                        if graph[r1][c1][1] != 0:
                            graph[r1][c1] = [merge_code, graph[r1][c1][1]]
                            graph[r2][c2] = [merge_code, graph[r1][c1][1]]
                        elif graph[r1][c1][1] == 0:
                            graph[r2][c2] = [merge_code, graph[r2][c2][1]]
                            graph[r1][c1] = [merge_code, graph[r2][c2][1]]

        elif c[0:6] == 'UNMERGE':

        else:


    return answer
