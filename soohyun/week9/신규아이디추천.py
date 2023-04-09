def solution(new_id: str) -> str:
    answer = []
    for char in new_id:
        if char.isalpha():
            answer.append(char.lower())
        elif char.isdigit():
            answer.append(char)
        elif char == ".":
            if answer and answer[-1] != ".":
                answer.append(char)
        elif char in ("-", "_"):
            answer.append(char)
    while answer and answer[-1] == ".":
        answer.pop()
    if not answer:
        answer.append("a")
    while len(answer) >= 16 or (answer and answer[-1] == "."):
        answer.pop()
    while len(answer) <= 2:
        answer.append(answer[-1])

    return ''.join(answer)

