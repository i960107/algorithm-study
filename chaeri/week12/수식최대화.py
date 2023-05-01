import re
import itertools

def solution(expression):
    operators = list(itertools.permutations(['-', '+', '*'], 3))
    expression = re.split('[-+*]', expression)

    result = []
    for operator in operators:
        arr = expression[:]
        for op in operator : 
            while op in arr:
                idx = arr.index(op)
                arr[idx-1] = str(eval(arr[idx-1]) + op  + arr[idx+1])
                del arr[idx:idx+2]
        result.append(abs(int(arr[0])))
    return max(result)