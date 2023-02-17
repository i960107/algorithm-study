# O(N^5).N은 각 자리에 올 수 있는 글자의 수.
# 각자리에 올 수 있는 모음(공백포함) 6가지라고 하면, 러프하게 6^5 = 7,776
# 실제로는 UUUUU까지 총 3905개

def solution(target: str) -> int:
    max_len = 5
    order = ["A", "E", "I", "O", "U"]
    index = {
        "A": 0,
        "E": 1,
        "I": 2,
        "O": 3,
        "U": 4,
    }

    word = []
    sequence = 0
    while True:
        if ''.join(word) == target:
            break

        sequence += 1

        if len(word) < max_len:
            word.append(order[0])
            continue

        while index[word[-1]] + 1 >= len(order):
            word.pop()
            j
        # while word[-1] == "U":
        #     word.pop()

        word[-1] = order[index[word[-1]] + 1]

    return sequence


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))
print(solution("UUUUU"))
