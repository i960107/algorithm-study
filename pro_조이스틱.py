# 풀이 중..
def solution(name):

    answer = 0

    moves = len(name) - 1

    for idx, value in enumerate(name):

        answer += min(ord(value) - ord('A'), ord('Z') - ord(value) + 1)

    answer += moves
    return answer
