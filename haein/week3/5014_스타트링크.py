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

answer = bfs(s, 0)
print(answer)

'''
고민했던 부분 
1. 시간 초과 -> 계산 결과 반복 안하도록 visited 처리
visited를 써서 이미 계산된 결과에 대해 다시 그것을 구하는 최단 거리를 반복하지 않도록 해줘야 함
그런데 어떻게 계산 거리를 visited로 처리해주어야 하나?
-> 어차피 계산 결과는 1 ~ f 이하의 수 중 하나 이므로 visited = [False for _ in range(f+1)]

2. while문 내에서 답이 나오지 않을 때 -> print문 대신 함수 return문의 활용으로 종료
처음에는 타겟을 발견하면 print로 종료시켜주었음
그러나 그렇게 하니 while문 내에서 타겟을 발견하지 못했을 때 어떻게 해줘야 할지 모르겠었음
그러면 print가 아니라 return문을 써야 함! (앞으로도 함수의 리턴문을 적극적으로 쓰자)
타겟 발견시 bfs()의 리턴값을 해당 cnt로 하고, 만약 while 내부에서 타겟 미발견 시엔 그 밖에 return을 두어서 해결함
'''
