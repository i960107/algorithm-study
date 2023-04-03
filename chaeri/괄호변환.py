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


    
def solution(p):
    answer = ''
    return answer