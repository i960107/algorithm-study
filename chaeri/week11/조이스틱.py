def solution(name):
    answer = 0 #조이스틱 조작횟수
    check = len(name) - 1
    
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1) #알파벳 변경 최솟값
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        check = min([check, 2 *i + len(name) - next, i + 2 * (len(name) - next)]) #최솟값 개신
    answer += check
    return answer