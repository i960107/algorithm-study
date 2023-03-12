from typing import List
import heapq


def solution(alp: int, cop: int, problems: List[List[int]]) -> int:
    # 문제를 풀거나, 시간을 쓰거나.
    # 왜 런타임 에러 발생하지. 어디서 발생할 수 있을까..
    queue = []
    n = len(problems)
    # costs행렬 초기화하기 위한 행렬의 길이
    alp_goal, cop_goal = max(x[0] for x in problems), max(x[1] for x in problems)

    for idx, (alp_req, cop_req, alp_rwd, cop_rwd, cost) in enumerate(problems):

        if alp_req <= alp and cop_req <= cop:
            # 문제를 풀고 나 후 상태
            nxt_alp, nxt_cop, nxt_cost = alp + alp_rwd, cop + cop_rwd, cost

        elif alp_req > alp and cop_req > cop:
            nxt_alp, nxt_cop, nxt_cost = alp_req, cop_req, alp_req - alp + cop_req - cop

        elif alp_req > alp:
            nxt_alp, nxt_cop, nxt_cost = alp_req, cop, alp_req - alp

        elif cop_req > cop:
            nxt_alp, nxt_cop, nxt_cost = alp, cop_req, cop_req - cop

        if nxt_alp > alp_goal:
            nxt_alp = alp_goal

        if nxt_cop > cop_goal:
            nxt_cop = cop_goal

        heapq.heappush(queue, (nxt_cost, nxt_alp, nxt_cop))

    INF = int(1e9)
    costs = [[INF] * (cop_goal + 1) for _ in range(alp_goal + 1)]

    while queue:
        cost_now, alp_now, cop_now = heapq.heappop(queue)

        # 왜....
        # 여기를 삭제하니깐 통과됨.?
        # 처음에 들어온 값이 alp + alp_rwd이 index out of range일 수 있음!
        if costs[alp_now][cop_now] < cost_now:
            continue

        for i in range(n):
            nxt_alp_req, nxt_cop_req, nxt_alp_rwd, nxt_cop_rwd, cost = problems[i]

            if alp_now < nxt_alp_req or cop_now < nxt_cop_req:
                nxt_alp, nxt_cop, nxt_cost = alp_now, cop_now, cost_now
                if alp_now < nxt_alp_req:
                    nxt_alp = nxt_alp_req
                    nxt_cost += (nxt_alp_req - alp_now)
                if cop_now < nxt_cop_req:
                    nxt_cop = nxt_cop_req
                    nxt_cost += (nxt_cop_req - cop_now)
            else:
                nxt_alp, nxt_cop, nxt_cost = alp_now + nxt_alp_rwd, cop_now + nxt_cop_rwd, cost_now + cost

            # 꼭 해당 점수 아니어도 됨. 더 클수도 있음..
            # 목표로 하는 점수를 넘어간다면 마지막 인덱스에 저장해주기
            if nxt_alp > alp_goal:
                nxt_alp = alp_goal

            if nxt_cop > cop_goal:
                nxt_cop = cop_goal

            if costs[nxt_alp][nxt_cop] <= nxt_cost:
                continue

            costs[nxt_alp][nxt_cop] = nxt_cost
            heapq.heappush(queue, (nxt_cost, nxt_alp, nxt_cop))

    return costs[alp_goal][cop_goal]


print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))
