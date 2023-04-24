from typing import List
import heapq


def solution(plans: List[str]):
    answer = []
    paused = []
    queue = []

    def convert_to_minutes(s: str) -> int:
        hh, mm = map(int, s.split(":"))
        return hh * 60 + mm

        # 시작시작이 빠른 순으로 정렬하기 위해 우선순위 큐를 사용

    # 시간 문자열을 분으로 변환
    for name, start, playtime in plans:
        heapq.heappush(queue, (convert_to_minutes(start), int(playtime), name))

    t = 0
    # 현재 진행중인 작업과 남은 시간
    now, left = None, 0

    # 문제에서 23:59 사이의 값만 들어간다고 했는데 하루를 기준으로 하는게 아님
    # 모든 작업이 끝날때까지 진행
    # while t <= (86,400):
    while t <= (60 * 24 * 1000):
        # 혀재 진행중인 작업이 끝났다면 처리
        if now and left == 0:
            answer.append(now)
            now, left = None, 0

        # 새로운 작업 시작해야 한다면 기존 작업 중단
        # 우선순위 새로 시작하는 작업 > 일시중지한 작업
        if queue and queue[0][0] == t:
            if now:
                paused.append((now, left))
            _, left, now = heapq.heappop(queue)
            print("새로시작", t, now, left)

        # 현재 하고 있는 작업 없다면(기존에 진행중인 작업도 없고, 새로 시작한 작업도 없을떼)
        if not now and paused:
            now, left = paused.pop()
            print("이어서", t, now, left)

        if now:
            left -= 1
        t += 1

    return answer
