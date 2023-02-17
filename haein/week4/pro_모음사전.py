from itertools import product
def solution(word):
    answer = 0
    arr = []

    for i in range(1, 6):
        for j in product([ 'A', 'E', 'I', 'O', 'U'], repeat = i):
            arr.append("".join(j))
    arr.sort()

    answer = arr.index(word) + 1

    return answer
