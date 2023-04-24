from collections import deque
from itertools import combinations


def solution_fail(name: str) -> int:
    movement = 0

    # 알파벳만 변경하는 횟수
    for alpha in name:
        alpha_move = min(ord(alpha) - ord("A"), 26 - (ord(alpha) - ord("A")))
        movement += alpha_move

    # 이동하는 횟수
    a_indices = [index for index in range(len(name)) if name[index] == "A"]
    for index1, index2 in combinations(a_indices, 2):
        pass

    min_move = len(name)

    movement += min_move
    return movement


solution_fail("ABBAABBBA")


def solution(name):
    # 조이스틱 조작 횟수
    answer = 0

    for i, now in enumerate(name):
        # 해당 알파벳 변경 최솟값 추가
        answer += min(ord(now) - ord('A'), ord('Z') - ord(now) + 1)

    # 최대 이동 횟수:  가장 마지막 A가 아닌 값까지 직진
    min_move = len(name) - 1
    for now, char in enumerate(name):
        # 연속된 A의 첫 시작 A만 비교
        if char != "A" or now > 0 and name[now - 1] == "A":
            continue

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = now + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        # now == 0인 경우 주의. A로 시작하는 경우
        # nxt == len(name)인 경우 주의 A로 끝나는 경우
        # BA처럼 첫번째글자가 A가 아니지만 두번째부터 A로시작하는 경우 주의
        if now <= 1 and next == len(name):
            min_move = 0
            break

        elif now <= 1:
            min_move = min(min_move, len(name) - next)

        elif next == len(name):
            min_move = min(min_move, now - 1)

        else:
            forth_and_back = 2 * (now - 1) + len(name) - next
            back_and_forth = (now - 1) + 2 * (len(name) - next)
            min_move = min(min_move, forth_and_back, back_and_forth)

    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    print(min_move)
    answer += min_move
    return answer


# print(solution("JEROEN"))
# print(solution("JAN"))
# print(solution("AAAABABAAAA"))
# print(solution("AAAA"))
# print(solution("JABAAAAB"))
# print(solution("BBBA"))
# print(solution("AAB"))
# print(solution("BAABAA"))
# print(solution("ZAAAZZZZZZZ"))
# print(solution("BBBAAAAAAAAAAB"))
# print(solution("CCAAC"))
# print(solution("AZAAZ`kj"))
# print(solution("AABAAAAAAABBB"))
# print(solution("BBAABAAAAB"))
# print(solution("BABAAABBBBB"))
# print(solution("ABAAAAAAAAABB"))
print(solution("BAAAAAABABA"))
