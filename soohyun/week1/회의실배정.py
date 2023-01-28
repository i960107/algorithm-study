from typing import List, Tuple
from sys import stdin


def solution(immediate_closing: int, meetings: List[Tuple[int]]) -> int:
    count = 0
    # 종료 시간이 같다면, 현재 시간 이후에 시작하는 어떤 회의를 선택해도 괜찮다고 생각
    # 끝나는 시간, 삽입된 순서대로 정렬됨.
    # 종료시간이 같으면서 시작하자 마자 끝나는 회의는 무조건 선택되어야 하는데 선택되지 않는 경우 생김.
    # 예를 들어 (3, 3), (1, 3)으로 정렬된 경우 두 회의 모두 진행될 수 있지만 한 회의만 진행되는 경우 생김.
    # 시작시간과 종료시간이 같더라도 다른 회의 중간에는 회의 진행될 수 없기때문에 미리 입력받으면서 시작시간과 종료시간이 같은 경우 빼놓는 것 좋은 선택이 아님.
    # meetings.sort(key=lambda x: x[1])

    # 종료 시간이 같다면, 먼저 시작한 걸 선택해야 함.
    meetings.sort(key=lambda x: (x[1], x[0]))

    time = 0

    for start, end in meetings:
        # 끝나는 시간이 같다면, 먼저 시작한 걸 선택.
        if start >= time:
            count += 1
            time = end
    return count


read = stdin.readline

n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, read().split())
    meetings.append((start, end))

print(solution(n, meetings))
