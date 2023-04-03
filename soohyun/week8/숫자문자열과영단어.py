def solution(s: str) -> int:
    dictionary = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    answer = 0
    temp = ''
    for char in s:
        if temp in dictionary:
            answer = answer * 10 + dictionary[temp]
            temp = ''

        if char.isdigit():
            answer = answer * 10 + int(char)
        else:
            temp += (char)
    if temp:
        answer = answer * 10 + dictionary[temp]
        temp = ''
    return answer


print(solution("one4seveneight"))
print(solution("23four5six7"))
