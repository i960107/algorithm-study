def solution(name: str) -> int:
    movement = 0

    for alpha in name:
        alpha_move = min(ord(alpha) - ord("A"), 26 - (ord(alpha) - ord("A")))
        movement += alpha_move

    min_not_A_index = 21
    max_not_A_index = -1

    for index, alpha in enumerate(name):
        # 가장 앞글자는 움직이지 않고도 조종 가능.
        if index == 0:
            continue
        if alpha != "A":
            min_not_A_index = min(min_not_A_index, index)
            max_not_A_index = max(max_not_A_index, index)

    # 좌우 방향 전환시 바꿔야하는 알파벳이 나오기까지 좌우 거리를 구하고 그 중 최소갑이 되는 방향으로 전환한다.
    if min_not_A_index != 21 and max_not_A_index != -1:
        curr = min(max_not_A_index, len(name) - min_not_A_index)
        movement += curr
    return movement


# print(solution("JEROEN"))
# print(solution("JAN"))
# print(solution("JAZ"))
# print(solution("AAA"))
# print(solution("LMNO"))
# 오른쪽으로 갔다가 다시 돌아가는게 더 나을 때도 있음!
print(solution("BBAAAAAAAAAAB"))
