from typing import List


# template1이나 template2로 풀면 안되는 이유?
# cut_tree == required가 되는 값이 없는 경우에 정확한 값이 반환되지 않음.
def solution(n: int, required: int, trees: List[int]) -> int:
    lo, hi = 0, max(trees)

    # cut_tree >= required인 값 중 최대값
    # cut_tree == required가 되는 값이 없다면 hi를 반환
    while lo <= hi:

        mid = lo + (hi - lo) // 2
        cut_tree = get_cut_tree(mid, trees)

        if cut_tree == required:
            return mid

        if cut_tree > required:
            lo = mid + 1

        else:
            hi = mid - 1

    # tmmplate1과 다른점. 정확히 일치하는 값이 없더라도 반환 값 있음.
    return hi


# 불가능.
def solution2(n: int, required: int, trees: List[int]) -> int:
    lo, hi = 0, max(trees)

    # cut_tree >= required인 값 중 최대값
    # 등호를 어디에 넣어야할까..
    # cut_tree == required가 되는 값이 없다면 어떻게 되지?
    while lo <= hi:

        mid = lo + (hi - lo) // 2
        cut_tree = get_cut_tree(mid, trees)

        if cut_tree == required:
            return mid

        if cut_tree > required:
            lo = mid + 1

        else:
            hi = mid - 1

    return hi


def get_cut_tree(h: int, trees: List[int]) -> int:
    return sum(t - h if t >= h else 0 for t in trees)


# 잘라진 나무 길이의 합이 required 이상이라는 조건을 만족하는 값들 중 최대값을 구하기 -> Parametric Search.
# 최적화 문제를 결정문제로 바꿔 푸는 탐색 알고리즘.
n, required = map(int, input().split())
tree = list(map(int, input().split()))
print(solution(n, required, tree))
