from typing import List


def solution(msg: str) -> List[int]:
    answer = []
    d = {chr(i): i - ord("A") + 1 for i in range(ord("A"), ord("Z") + 1)}
    sequence = ord("Z") - ord("A") + 1

    temp = ""
    start, end = 0, 0
    while end < len(msg):
        if temp + msg[end] not in d:
            sequence += 1
            d[temp + msg[end]] = sequence
            answer.append(d[temp])
            start += 1
            temp = ""
            continue
        temp += msg[end]
        end += 1
    answer.append(d[temp])

    return answer
