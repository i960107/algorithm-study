from typing import List


def solution(commands: List[str]) -> List[str]:
    value_d = dict()
    board = [[((row - 1) * 50 + col) if row != 0 and col != 0 else 0 for col in range(51)] for row in range(51)]
    ids = 50 * 50

    def _print(r: int, c: int) -> str:
        r, c = int(r), int(c)
        area_id = board[r][c]
        return value_d[area_id] if area_id in value_d else "EMPTY"

    def merge(r1: int, c1: int, r2: int, c2: int):
        r1, r2, c1, c2 = int(r1), int(r2), int(c1), int(c2)
        if r1 == r2 and c1 == c2:
            return
        target_id = board[r2][c2]
        target_value = None
        if target_id in value_d:
            target_value = value_d.pop(target_id)
        area_id = board[r1][c1]
        board[r2][c2] = area_id
        if area_id not in value_d and target_value:
            value_d[area_id] = target_value

    # unmerge 인접한 구역 아닌 경우있어서 dfs로 풀면 안됨!!!
    def unmerge(r: int, c: int):
        r, c = int(r), int(c)
        area_id = board[r][c]
        nonlocal ids
        for nr in range(1, 51):
            for nc in range(1, 51):
                if (r != nr or c != nc) and board[nr][nc] == area_id:
                    ids += 1
                    board[nr][nc] = ids

    def update_value(r: int, c: int, value: int):
        r, c = int(r), int(c)
        area_id = board[r][c]
        value_d[area_id] = value

    def update_values(value1: int, value2: int):
        for r in range(1, 51):
            for c in range(1, 51):
                area_id = board[r][c]
                if area_id in value_d and value_d[area_id] == value1:
                    value_d[area_id] = value2

    answer = []
    for command in commands:
        move, *args = command.split()
        if move == "UPDATE":
            if len(args) == 2:
                update_values(*args)
            else:
                update_value(*args)
        elif move == "MERGE":
            merge(*args)
        elif move == "UNMERGE":
            unmerge(*args)
        else:
            answer.append(_print(*args))
    return answer


# union find?


# print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice",
#                 "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant",
#                 "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4",
#                 "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
# print(solution(
#     ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1",
#      "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))

# 반례 -> 이미 병합된 셀을 다시 병합할때, 그 전체 영역이 하나의 영역이 되는게 아님
print(solution(
    ["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4", "MERGE 1 1 4 4",
     "UNMERGE 3 3", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]))
