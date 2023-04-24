#분리하기
def divide(w):
    start = 0
    end = 0
    for i in range(len(w)):
        if w[i] == '(':
            start += 1
        else:
            end += 1
        if start == end:
            return w[:i + 1], w[i + 1:]

#체크하기
def check(u):
    q = []
    for x in u:
        if not q:
            q.append(x)
        else:
            if x == ')' and q[-1] == '(':
                q.pop()
            else:
                q.append(x)
    if q:
        return False
    return True

def solution(p):
    if p == '':
        return p
    u, v = divide(p)
    if check(u):
        return u + solution(v)
    else:
        temp = '('+solution(v)+')'
        for x in u[1:-1]:
            if x == '(':
                temp += ')'
            else:
                temp += '('
        return temp
    