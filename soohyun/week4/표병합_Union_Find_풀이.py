from typing import List, Dict, Tuple


# 2차원 배열에서의 union-find어떻게?
def find(parent: List[List[Tuple[int, int]]], r: int, c: int) -> Tuple[int, int]:
    if parent[r][c] != (r, c):
        # 그 아이디가 가리키는 칸을 찾아가야하는데..
        parent[r][c] = find(parent, *parent[r][c])
    return parent[r][c]


def union(parent: List[List[Tuple[int, int]]], r1: int, c1: int, r2: int, c2: int):
    r1, c1 = find(parent, r1, c1)
    r2, c2 = find(parent, r2, c2)
    if r1 == r2 and c1 == c2:
        return
    if r1 < r2 or (r1 == c1 and c1 < c2):
        parent[r2][c2] = (r1, c1)
    else:
        parent[r1][c1] = (r2, c2)


def solution(commands: List[str]) -> List[str]:
    value_d = dict()
    parent = [[(row, col) if row != 0 and col != 0 else 0 for col in range(51)] for row in range(51)]
    ids = [[(row - 1) * 50 + col if row != 0 and col != 0 else 0 for col in range(51)] for row in range(51)]

    def _print(r: str, c: str) -> str:
        r, c = int(r), int(c)
        parent_r, parent_c = parent[r][c]
        id = ids[parent_r][parent_c]
        return value_d[id] if id in value_d else "EMPTY"

    def merge(r1: str, c1: str, r2: str, c2: str):
        r1, r2, c1, c2 = int(r1), int(r2), int(c1), int(c2)
        union(parent, r1, c1, r2, c2)

    def unmerge(r: str, c: str):
        r = int(r)
        c = int(c)
        if parent[r][c] != (r, c):

    def update_value(r: str, c: str, value: str):
        r, c = int(r), int(c)
        area_id = ids[r][c]
        value_d[area_id] = value

    def update_values(value1: str, value2: str):
        for r in range(1, 51):
            for c in range(1, 51):
                area_id = ids[r][c]
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


print(solution(
    ["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4", "MERGE 1 1 4 4",
     "UNMERGE 3 3", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]))
