from typing import List


def solution_fail(key: List[List[int]], lock: List[List[int]]) -> bool:
    n = len(lock)

    def make_bin(arr: List[List[int]]):
        bin_arr = []
        for row in arr:
            temp = 0
            for index in range(len(row)):
                temp = temp * 2 + row[index]
            bin_arr.append(temp)
        return bin_arr

    row_goal = 1 << (n - 1)

    def _solution(bin_key, bin_lock):
        for shift_horizontal in range(-n, n):
            for shift_vertical in range(-n, n):
                found = True
                for r, row_lock in enumerate(bin_lock, 1):
                    if shift_vertical >= 0 and shift_vertical <= r:
                        if shift_horizontal < 0:
                            row_key = bin_key[r - shift_vertical] << abs(shift_horizontal)
                        else:
                            row_key = bin_key[r - shift_vertical] >> abs(shift_horizontal)
                    else:
                        row_key = 0

                    if (row_key ^ row_lock != row_goal):
                        found = False
                        break
                if found:
                    return True
        return False

    bin_lock = make_bin(lock)

    def rotate(arr):
        n = len(arr)
        result = []
        for c in range(n):
            row = []
            for r in range(n - 1, -1, -1):
                row.append(arr[r][c])
            result.append(row)
        return result

    bin_lock = make_bin(lock)
    bin_key = make_bin(key)
    if _solution(bin_key, bin_lock):
        return True

    prev = key
    for _ in range(3):
        rotated = rotate(prev)
        if _solution(bin_key, bin_lock):
            return True

    return False


def solution(key: List[List[int]], lock: List[List[int]]) -> bool:
    def rotate(arr: List[List[int]]):
        n = len(arr)
        result = [[0] * n for _ in range(n)]

        for r in range(n - 1, -1, -1):
            for c in range(n):
                result[c][-r + n - 1] = arr[r][c]
        return result

    K = len(key)
    L = len(lock)

    def check(new_lock):
        # 최대 60 * 60 배열이므로 선형 탐색 가능.
        n = len(new_lock) // 3
        # 실제 의미있는 부분은 가운데 부분
        for i in range(n, n * 2):
            for j in range(n, n * 2):
                # 더해서 1이되어야 함
                if new_lock[i][j] != 1:
                    return False
        return True

    # 기존 key의 3배만큼의 크기를 선언, 좌, 우, 위,아래로 key이동후 인덱스 비교 쉽게 하기 위해서
    # lock이 key보다 큰 경우 있음
    new_lock = [[0] * (L * 3) for _ in range(L * 3)]
    for i in range(L):
        for j in range(L):
            new_lock[L + i][L + j] = lock[i][j]

    # 총 3번 돌리기
    for _ in range(4):
        # i,j는 key가 시작하는 위치. 1부터 시작해야 겹쳐지는 부분 생김
        # i, j == 1, 2 이면 key를 위로 2칸, 왼쪽으로 한칸
        for i in range(1, L * 2):
            for j in range(1, L * 2):
                for x in range(K):
                    for y in range(K):
                        new_lock[i + x][j + y] += key[x][y]

                if check(new_lock):
                    return True

                # 원래대로 되돌리기
                for x in range(K):
                    for y in range(K):
                        new_lock[i + x][j + y] -= key[x][y]
        key = rotate(key)
    return False
