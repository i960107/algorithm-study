def solution(n, m, x, y, r, c, k):
    answer = ''
    dist = abs(x-r)+abs(y-c)
    k -= dist
    if k < 0 or k%2 != 0:
        return "impossible"
    
    direction = {'d':0, 'l':0, 'r':0, 'u':0}
    if x > r:
        direction['u'] += x-r
    else:
        direction['d'] += r-x
    if y > c:
        direction['l'] += y-c
    else:
        direction['r'] += c-y
        
    answer += 'd'*direction['d']
    d = min(int(k/2), n-(x+direction['d']))
    answer += 'd'*d
    direction['u'] += d
    k -= 2*d
    
    answer += 'l'*direction['l']
    l = min(int(k/2), y-direction['l']-1)
    answer += 'l'*l
    direction['r'] += l
    k -= 2*l
    
    answer += 'rl'*int(k/2)
    answer += 'r'*direction['r']
    answer += 'u'*direction['u']
    return answer

# 효율성 검사 없지만 10초 이상.. 시간 초과
def solution_fail(n, m, x, y, r, c, k):
    answer = ''
    # 문자열이 사전 순으로 가장 빠른 경로로 탈출
    d = ("r", "l", "d", " u")
    dr = (0,0,1,-1)
    dc = (1, -1, 0, 0)
    def dfs(now_r, now_c, distance, path):
        nonlocal k, answer
        if distance == k:
            if now_r == r and now_c == c:
                answer = ''.join(path)
            return
        for k in range(4):
            nr, nc = now_r + dr[k], now_c + dc[k]
            if not(0 <= nr < n and 0 <= nc < m):
                continue
            path.append(d[k])
            dfs(nr, nc, distance + 1, path)
            path.pop()
            if answer != '':
                return
            
    dfs(x, y, 0, [])
    return answer if answer else 'impossible'

def solution_fail2(n:int, m:int, x:int, y:int, r:int, c:int, k:int) -> str:
    answer = ''
    # 사전순 -> d, l, r, u
    min_move = abs(x - r) + abs(c - y)
    if min_move > k or (k - min_move) % 2 != 0:
        return 'impossible'
    left = right = up = down = 0
    if x <= r:
        down += (r - x)
    else:
        up += (x - r)
    if y <= c:
        right += (c - y)
    else:
        left += (y - c)
    extra = (k - min_move) // 2
    if r < n:
        down += extra
        up += extra
    elif c > 1 or c < m:
        left += extra
        right += extra
    else:
        down += extra
        up += extra
    
    print(down, left, right, up)
    return "d" * down + 'l' * left + "r" * right + "u" * up


