def solution(name: str) -> int:
    joystick = []
    movement = 0

    for alpha in name:
        alpha_move = min(ord(alpha) - ord("A"), 26 - (ord(alpha) - ord("A")))
        movement += alpha_move
        joystick.append(alpha_move)

    print(movement)
    min_not_A_index = 21
    max_not_A_index = -1

    for index, alpha in enumerate(name):
        if alpha != "A":
            min_not_A_index = min(min_not_A_index, index)
            max_not_A_index = max(max_not_A_index, index)

    if min_not_A_index != 21 and max_not_A_index != -1:
        print(max_not_A_index, len(name) - min_not_A_index)
        curr = min(max_not_A_index, len(name) - min_not_A_index)
        movement += curr
    print(min_not_A_index, max_not_A_index, curr)
    return movement


print(solution("JEROEN"))
print(solution("JAN"))
# print(solution("JAZ"))
# print(solution("AAA"))
