from functools import cmp_to_key
# compare함수를 통해 위치를 변경(1은 앞으로, -1은 뒤로 정렬)
def compare(x, y):
    if x+y > y+x:
        return -1
    elif x+y == y+x:
        return 0
    else:
        return 1

def solution(numbers):
    numbers  = list(map(str, numbers))
    numbers = sorted(numbers, key=cmp_to_key(compare))
    return str(int(''.join(numbers)))




