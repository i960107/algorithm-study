from collections import deque
f, s, g, u, d = map(int, input().split())
visited = [False for _ in range(f+1)]

def bfs(start_v, start_cnt):
    queue = deque([(start_v, start_cnt)])
    visited[start_v] = True

    while queue:
        tmp, tmp_cnt = queue.popleft()

        if tmp == g:
            return tmp_cnt # bfs 함수 종료
        else:
            tmp_cnt += 1
            if 1 <= tmp + u <= f and not visited[tmp + u]:
                visited[tmp + u] = True
                queue.append((tmp+u, tmp_cnt))
            if 1 <= tmp - d <= f and not visited[tmp -d]:
                visited[tmp -d] = True
                queue.append((tmp-d, tmp_cnt))

    # while문이 끝나도 return으로 종료되지 않으므로 bfs 함수가 아직 종료되지 않았음
    # while문 다음에 return 달아주기!
    return 'use the stairs'

print(bfs(s, 0))

