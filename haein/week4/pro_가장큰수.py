def solution(numbers):
    answer = ''

    sorted_numbers = sorted(numbers, key = lambda x : str(x)*3, reverse = True)

    answer = str(int("".join(str(i) for i in sorted_numbers)))

    return answer
'''
문자열로 되어있는 수의 경우 인덱스 앞쪽부터 ascii 코드로 변환하여 대소 비교 따짐
x*3 하는 이유는 가장 큰 수가 1000이기 때문에 인덱스 비교 시 끝까지 비교할 수 있게 해주려고
'''
