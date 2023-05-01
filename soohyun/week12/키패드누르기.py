def solution(numbers, hand):
    # 왼손 엄지 위치
    lr, lc = 3, 0
    # 오른손 엄지 위치
    rr, rc = 3, 2

    # 키패드 별 2차원 배열의 위치
    d = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        0: (3, 1),
    }

    answer = []
    for number in numbers:
        if number in (1, 4, 7):
            lr, lc = d[number]
            answer.append("L")
        elif number in (3, 6, 9):
            rr, rc = d[number]
            answer.append("R")
        else:
            l_distance = abs(lr - d[number][0]) + abs(lc - d[number][1])
            r_distance = abs(rr - d[number][0]) + abs(rc - d[number][1])
            if l_distance > r_distance:
                rr, rc = d[number]
                answer.append("R")
            elif l_distance < r_distance:
                lr, lc = d[number]
                answer.append("L")
            else:
                if hand == "left":
                    lr, lc = d[number]
                    answer.append("L")
                elif hand == "right":
                    rr, rc = d[number]
                    answer.append("R")

    return ''.join(answer)
