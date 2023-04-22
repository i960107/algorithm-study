from typing import List
from itertools import permutations


# brute-force로 모든 조합 탐색 후 최소 방법 선택.
# 시작하는 취약 포인트 * 방향(시계, 반시계) * dist순서
#  15 * 2 * 8! * 15 = 18,144,000
def solution_fail(n: int, weak: List[int], dist: List[int]) -> int:
    min_required = n
    # 랜덤으로 dist 정렬
    for x in permutations(dist):
        min_required = min(min_required, get_min_required_count_to_cover_all(n, weak, list(x)))
    return min_required


# 취약 지점을 전부 점검하기 위해 필요한 최소한의 사람.
def get_min_required_count_to_cover_all(n: int, weak: List[int], dist: List[int]) -> int:
    # 시계방향으로 cover

    min_required = n

    for start in range(len(weak)):
        clockwise_required = get_required_count_to_cover_all_clockwise(n, start, weak, dist)
        counter_clockwise_required = get_required_count_to_cover_all_counter_clockwise(n, start, weak, dist)
        min_required = min(min_required, clockwise_required, counter_clockwise_required)

    return min_required


def get_required_count_to_cover_all_clockwise(n: int, start: int, weak: List[int], dist: List[int]) -> int:
    person = -1
    # weak[start]를 기준으로 떨어진 거리로 나타낸 커버된 거리.
    covered = -1
    for temp in range(start, start + len(weak)):
        # start를 0으로 본다면,
        temp_point = weak[temp % len(weak)]
        # start point로부터 떨어진 거리
        point = temp_point - weak[start] if temp_point >= weak[start] else n - weak[start] + temp_point
        if point <= covered:
            continue
        person += 1
        if person >= len(dist):
            return -1
        covered = point + dist[person]
    return person + 1


def get_required_count_to_cover_all_counter_clockwise(n: int, start: int, weak: List[int], dist: List[int]) -> int:
    person = -1
    covered = -1
    for temp in range(len(weak)):
        # start를 0으로 본다면,
        temp_point = weak[start - temp]
        point = weak[start] - temp_point if temp_point <= weak[start] else n - temp_point + weak[start]
        if point <= covered:
            continue
        person += 1
        if person >= len(dist):
            return -1
        covered = point + dist[person]
    return person + 1


# 이건 counter_clockwise고려하지 않은 것 아닌가?
# 모든 친구들이 같은 방향으로 돌 필요는 없음.
def solution(n, weak, dist):
    W, F = len(weak), len(dist)
    repair_lst = [()]  # 현재까지 고칠 수 있는 취약점들 저장 (1,2,3)
    count = 0  # 투입친구 수
    dist.sort(reverse=True)  # 움직일 수 있는 거리가 큰 친구 순서대로
    # dist.sort() # 실패 왜지.. 모든 가능한 경우 중에서 투입 친구 수가 가장 적은 수를 구해야 하기 때문에...
    # greedy하게 생각해서 가장 긴 거리를 이동할 수 있는 친구를 가장 먼저 투입하는 것이 나음

    # 고칠 수 있는 것들 리스트 작성
    for can_move in dist:
        repairs = []  # 친구 별 고칠 수 있는 취약점들 저장
        count += 1

        # 수리 가능한 지점 찾기
        # A -> B로 도나, B->A로 도나 같은 경우임...
        # 시계 방향을 커버할 수 있는 경우만 생각
        for i, wp in enumerate(weak):
            start = wp  # 각 위크포인트부터 시작
            ends = weak[i:] + [n + w for w in weak[:i]]  # 시작점 기준 끝 포인트 값 저장
            can = [end % n for end in ends if end -
                   start <= can_move]  # 가능한 지점 저장
            repairs.append(set(can))

        # 수리 가능한 경우 탐색
        cand = set()
        for r in repairs:  # 새친구의 수리가능 지점
            for x in repair_lst:  # 기존 수리가능 지점
                new = r | set(x)  # 새로운 수리가능 지점
                if len(new) == W:  # 모두 수리가능 한 경우 친구 수 리턴
                    return count
                cand.add(tuple(new))
        repair_lst = cand

    return -1


def solution2(n: int, weak: List[int], dist: List[int]) -> int:
    W = len(weak)
    F = len(dist)

    count = 0
    dist.sort(reverse=True)
    repair_combi = [set()]

    for d in dist:
        count += 1

        # 가장 처음에 repair_combi == []일때 주의! 빈 set 넣어주기
        repairs = []
        for w in weak:
            start = w
            repairs.append(
                set([point for point in weak if (point - start if start <= point else n - start + point) <= d]))

        new_repair_combi = []
        for prev in repair_combi:
            for curr in repairs:
                combi = prev | curr
                if len(combi) == W:
                    return count
                new_repair_combi.append(combi)
        repair_combi = new_repair_combi

    return -1

