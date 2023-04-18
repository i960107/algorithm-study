def solution(p: str) -> str:
    if p == "":
        return p
    left = right = 0
    u = v = None
    for index, char in enumerate(p):
        if char == "(":
            left += 1
        else:
            right += 1
        if left == right:
            u = p[:index + 1]
            v = p[index + 1:]
            break
            
    def is_valid_bracket(s:str) -> bool:
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        return not stack
    
    if is_valid_bracket(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ")" + ''.join("(" if x == ")" else ")" for x in u[1:-1])
    

