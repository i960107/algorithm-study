def solution(s: str) -> int:
    answer = len(s)
    # 최대 압축 단위 글자수의 반까지. 그 이상은 압축효과 없음
    for unit in range(1, len(s) // 2 + 1):
        compressed = []
        temp = ""
        count = 0
        for start_index in range(0, len(s), unit):
            now = s[start_index:start_index + unit]
            if now == temp:
                count += 1
            else:
                if count > 1:
                    compressed.append(str(count))
                compressed.append(temp)
                count = 1
                temp = now
        if count > 1:
            compressed.append(str(count))
        compressed.append(temp)

        result = ''.join(compressed)

        if len(result) < answer:
            answer = len(result)

    return answer
