from itertools import permutations


def solution(expression):
    ops = ("+", "-", "*")
    
    arr = []
    temp = []
    for char in expression:
        if char.isdigit():
            temp.append(char)
        else:
            arr.append(int(''.join(temp)))
            temp = []
            arr.append(char)
    arr.append(int(''.join(temp)))
    
        
    def calculate(priorities, arr):
        for p in range(3):
            op = priorities[p]
            temp = []
            for index, x in enumerate(arr):
                if temp and temp[-1] == op:
                    temp.pop()
                    num = temp.pop()
                    if op == "+":
                        temp.append(num + x)
                    elif op == "-":
                        temp.append(num - x)
                    elif op == "*":
                        temp.append(num * x)
                else:
                    temp.append(x)
            arr = temp
        return arr[0]
        
        
    max_result = -float("INF")
    for permutes in permutations(range(3), 3):
        priorities = {p: op for op, p in zip(ops, permutes)}
        result = calculate(priorities, arr)
        max_result = max(max_result, abs(result))
            
            
    return max_result
