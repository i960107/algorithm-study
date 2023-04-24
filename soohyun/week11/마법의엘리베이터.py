def solution_fail(storey):
    if storey < 10:
        return storey if storey <= 5 else 10 - storey + 1

    count = 0

    storey = str(storey)
    n = len(storey)

    higher_than = False
    for index in range(n - 1):
        now = storey[index]

        nxt_index = index + 1
        while nxt_index < n - 1 and storey[nxt_index] == "5":
            nxt_index += 1
        nxt = storey[nxt_index]

        if higher_than:
            if nxt <= "5":
                count += (10 - int(now))
                higher_than = False
            else:
                count += (10 - int(now) - 1)
        else:
            if nxt <= "5":
                count += (int(now))
            else:
                count += (int(now) + 1) if int(now) < 9 else 1
                higher_than = True

    if higher_than:
        count += (10 - int(storey[-1]))
    else:
        count += (int(storey[-1]))

    return count


def solution(storey):
    answer = 0

    # storey: 현재 층수. 0층될때까지 진행
    # answer에 현재까지 이동한 횟수를 누적해간다
    while storey:
        # 1의 자리수
        remainder = storey % 10

        # 5이상이면 10으로 이동하는게 가까움
        # 10으로 이동한다면 앞자리에 1을 더해줘야 함. ex) 2554 -> 2560
        if remainder > 5:
            answer += (10 - remainder)
            storey += (10)

        # 5이상이면 0으로 이동하는게 가까움
        elif remainder < 5:
            answer += remainder

        # 5라면 앞자리수까지 비교. 55 이상이라면 10으로 이동
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remainder

        # 1의 자리수 비교 끝남.
        storey //= 10
    return answer
