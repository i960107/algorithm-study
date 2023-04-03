from typing import List


def solution(id_list: List[str], report: List[str], k: int) -> List[int]:
    reports = dict([(x, set()) for x in id_list])
    users = dict([(name, index) for index, name in enumerate(id_list)])

    for info in report:
        reporter, reportee = info.split()
        reports[reportee].add(reporter)

    answer = [0] * len(id_list)

    for user, reporters in reports.items():
        if len(reporters) < k:
            continue
        for reporter in reporters:
            index = users[reporter]
            answer[index] += 1
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
