from typing import List
from collections import deque


# 효율성테스트 있다면 복잡도 계산해서 알고리즘 짜기
# 총 이동 -> 1,000,000 효율성 테스트 통과 가능
# runtime error?
# 마지막 상태를 기억?


def solution_fail(n: int, k: int, cmd: List[str]) -> str:
    DELETED = -1
    #
    left = deque([i for i in range(k)])
    right = deque([i for i in range(k, n)])
    # stack
    deleted = []

    # pointer는 항상 right의[0]을 가리킴
    # 복구가 어려움...
    for command in cmd:
        if command[0] == "D":
            for _ in range(int(command.split()[1])):
                left.append(right.popleft())

        elif command[0] == "U":
            # 포인터가 첫번째 행을 가르키는 경우 left = []일 수 있음
            # right는 빌 수 없음
            for _ in range(int(command.split()[1])):
                right.appendleft(left.pop())

        # insertion -> O(N) -> 최대 500번  * 1,000,000
        elif command[0] == "Z":
            last_deleted = deleted.pop()
            if last_deleted < right[0]:
                insertion_index = 0
                for index, id in enumerate(left):
                    insertion_index = index
                    if id > last_deleted:
                        break
                if insertion_index == len(left) - 1 and left[insertion_index] < last_deleted:
                    left.append(last_deleted)
                else:
                    left.insert(insertion_index, last_deleted)
            else:
                insertion_index = 0
                for index, id in enumerate(right):
                    insertion_index = index
                    if id > last_deleted:
                        break
                if insertion_index == len(right) - 1 and right[insertion_index] < last_deleted:
                    right.append(last_deleted)
                else:
                    right.insert(insertion_index, last_deleted)

        elif command[0] == "C":
            deleted.append(right.popleft())
            if not right:
                right.appendleft(left.pop())

    answer = ["X"] * n
    for i in left:
        answer[i] = "O"
    for i in right:
        answer[i] = "O"
    return ''.join(answer)


# 왜 시간초과가 날까
# insertion쓰지 않는 방법 있을까?
# linkedlist랑 같지 않나?
def solution_fail2(n: int, k: int, cmd: List[str]) -> str:
    # deleted
    is_deleted = [False] * n
    # stack
    deleted_elements = []

    # table -> 왜 하나의 배열로 사용하지 않는지
    left = deque([i for i in range(k)])
    right = deque([i for i in range(k, n)])

    # right[0]은 항상 유효한(삭제되지 않은)element를 가리키고 있음? -> NO
    for command in cmd:
        if command[0] == "D":
            count = int(command.split()[1])
            while count > 0:
                element = right.popleft()
                left.append(element)
                count -= 1

        elif command[0] == "U":
            count = int(command.split()[1])
            while count > 0:
                element = left.pop()
                right.appendleft(element)
                count -= 1

        # 되돌리기가 가장 어려움. O(N)아닌 복잡도 가능?
        elif command[0] == "Z":

            last_deleted = deleted_elements.pop()
            is_deleted[last_deleted] = False
            if last_deleted < right[0]:
                insertion_index = 0
                for index, id in enumerate(left):
                    insertion_index = index
                    if id > last_deleted:
                        break
                if insertion_index == len(left) - 1 and left[insertion_index] < last_deleted:
                    left.append(last_deleted)
                else:
                    left.insert(insertion_index, last_deleted)
            else:
                insertion_index = 0
                for index, id in enumerate(right):
                    insertion_index = index
                    if id > last_deleted:
                        break
                if insertion_index == len(right) - 1 and right[insertion_index] < last_deleted:
                    right.append(last_deleted)
                else:
                    right.insert(insertion_index, last_deleted)

        elif command[0] == "C":
            element = right.popleft()
            deleted_elements.append(element)
            is_deleted[element] = True
            if not right:
                right.appendleft(left.pop())

    return ''.join(["X" if x else "O" for x in is_deleted])


def solution(n: int, k: int, cmd: List[str]) -> str:
    answer = ['O'] * n

    cur = k

    # prev, nxt
    # dict형으로 저장.
    table = {i: [i - 1, i + 1] for i in range(n)}
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]

    deleted = []

    for c in cmd:
        if c == "C":
            answer[cur] = "X"
            prev, nxt = table[cur]
            deleted.append([prev, cur, nxt])
            # 포인터 이동. 다음 원소가 없다면 바로 전 원소로
            if not nxt:
                cur = prev
            else:
                cur = nxt
            # linked_list 조정. cur 값들은 그대로 살려둠
            # 런타임 에러나는 이유?

            # if prev:
            #     table[prev][1] = nxt

            # if nxt:
            #     table[nxt][0] = prev

            if prev == None:
                table[nxt][0] = None

            elif nxt == None:
                table[prev][1] = None

            else:
                table[prev][1] = nxt
                table[nxt][0] = prev

        elif c == "Z":
            prev, now, nxt = deleted.pop()
            answer[now] = "O"

            # prev, nxt가 삭제되었을때는?
            # 가장 마지막에 삭제된 원소가 되돌려지는 것이기 때문에 prev, nxt가 변경되었을 가능성 없음!
            if prev:
                table[prev][1] = now

            if nxt:
                table[nxt][0] = now

        else:
            move, count = c.split()
            count = int(count)
            if move == "D":
                for _ in range(count):
                    cur = table[cur][1]

            elif move == "U":
                for _ in range(count):
                    cur = table[cur][0]

    return ''.join(answer)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
