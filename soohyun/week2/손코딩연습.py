from typing import List, Union, Optional
from bisect import bisect_left, bisect_right


# arr은 정렬된 상태여야 함. O(LogN)의 복잡도로 빠르게 탐색가능.
# template별 다른점
# 1) 반복문 종료 조건. 등호 포함/불포함 여부
# 2) 반복문 내에서 탐색되지 않는 원소의 개수 -> 반복문 내 조건문의 등호, 포인터 mid를 포함해서 이동, mid를 제외하고 이동
# 3) while문 밖에서 반환 값(post-processing)
# 4) 중복 시
# 5) 찾는 원소가 없을때


# template1
# 1) left <= right
# 2) 모든 원소 탐색함. left, right = mid + 1, mid - 1로 mid제외하고 이동. arr[mid] == target일 경우 반환
# 3) while문 종료되었다는 것은 찾는 원소가 존재하지 않는다는 것으로 -1을 반환
# 4) 중복된 원소중 하나 랜덤하게 반환
# 5) -1 반환

def binary_search_template1(arr: List[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mi - 1
    return -1


# template2:
# 1) left < right
# 2) 원소 하나 탐색 안함.
# 3) left==right 둘중 아무거나 확인.
# 4) 중복된 원소중 하나 랜덤하게 반환
# 5) -1 반환


def binary_search_template2(arr: List[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid

    # lo == hi ==> 확인 안된 원소
    if arr[lo] == target:
        return lo

    return -1


# 불가능한가? [2,3] target==3인 경우 생각해보기
def binary_search_template2_version2(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    # 모든 원소를 확인하고 나서 while문 빠져나옴.
    # right < left가 됨.

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        # 이미 검사한 항목은 제외.
        elif arr[mid] < target:
            left = mid
        elif arr[mid] > target:
            right = mid - 1

    if arr[left] == target:
        return left

    return - 1


# template3:
# 1) left < right - 1
# 2) 원소 2개 탐색 안함.
# 3) left,right 둘다 확인
# 4) 중복된 원소중 하나 랜덤하게 반환
# 5) -1 반환
def binary_search_template3(arr: List[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1

    # 탐색 범위 최소 길이 3
    while lo < hi - 1:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid
        else:
            hi = mid

    # left == right - 1에서 빠져나온 후 left, right 후처리 필요
    if arr[lo] == target:
        return lo
    if arr[hi] == target:
        return hi
    return - 1


# template2와 비슷.
def binary_search_bisect_left(arr: List[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid

    return lo


# 일치하지 않는 인덱스를 찾아야함
def binary_search_bisect_right(arr: List[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


# get_first_occurrence. template1과 비슷.
def binary_search_find_left(arr: List[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if (mid == 0 or arr[mid - 1] != target) and arr[mid] == target:
            return mid

        elif arr[mid] < target:
            lo = mid + 1

        else:
            hi = mid - 1

    return -1


def binary_search_find_right(arr: List[int], target: int, lo: int = 0, hi: Optional[int] = None) -> int:
    if hi is None:
        hi = len(arr) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if (mid == n - 1 or arr[mid + 1] != target) and arr[mid] == target:
            return mid

        elif arr[mid] > target:
            hi = mid - 1

        else:
            lo = mid + 1

    return -1


def insert_left(arr: List[int], target: int) -> int:
    # bisect_left: 중복원소가 있다면 가장 왼쪽 원소, 찾는 원소가 없다면 가장 가까운 작은 원소 뒤
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1

        elif arr[mid] >= target:
            right = mid

    return left


def insert_right(arr: List[int], target: int) -> int:
    # bisect_right
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] > target:
            right = mid

        elif arr[mid] <= target:
            left = mid + 1

    return left


def binary_search_haein_iterative(arr: List[int], target: int) -> Union[int, None]:
    # template1과 같은 방식
    arr.sort()
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
    return None


def binary_search_haein_recursive(arr: List[int], target: int, left: int, right: int) -> Union[int, None]:
    if left > right:
        return None

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_haein_recursive(arr, target, mid + 1, right)
    elif arr[mid] > target:
        return binary_search_haein_recursive(arr, target, left, mid - 1)


# 중복이 없는 경우: 출력값 (3,3,3)
print("1", binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
print("2", binary_search2_version1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
print("3", binary_search2_version2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))

# 중복이 있는 경우(2, 3,1)
print("4", binary_search([1, 2, 2, 2, 3], 2))
print("5", binary_search2_version1([1, 2, 2, 2, 3], 2))
print("6", binary_search2_version2([1, 2, 2, 2, 3], 2))

# 찾는 값이 없는 경우: -1을 반환. 아니면 0또는 n을 반환?(-1, -1, -1)
print("7", binary_search([1, 2, 2, 3], 4))
print("8", binary_search2_version1([1, 2, 2, 3], 4))
print("9", binary_search2_version2([1, 2, 2, 3], 4))

# bisect_module(1,4,5,5,0,0)
# bisect_module 찾는 값이 없을 경우 0 또는 마지막 인덱스 반환
print("10", bisect_left([1, 2, 2, 2, 3], 2, 0, 4))
print("11", bisect_right([1, 2, 2, 2, 3], 2, 0, 4))
print("12", bisect_left([1, 2, 2, 2, 3], 4, 0, 4))
print("13", bisect_right([1, 2, 2, 2, 3], 0, 0, 4))
print("14", bisect_left([1, 2, 2, 2, 3], 0, 0, 4))
print("15", bisect_right([1, 2, 2, 2, 3], 0, 0, 4))
