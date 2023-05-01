import sys

sys.setrecursionlimit(10 ** 6)

group = 1


# node를 루트노드로 한 서브트리에 대해서 key를 넘지 않는 크기의 그룹으로 나누었을때 그룹의 개수 -> group 갱신. 그룹의 크기 return
def exam_room(node, key, num, links):
    global group
    if node == -1:
        return 0
    # left_cnt, right_cnt에는 key를 넘지 않지 않음
    left_cnt = exam_room(links[node][0], key, num, links)
    right_cnt = exam_room(links[node][1], key, num, links)
    if left_cnt + right_cnt + num[node] <= key:
        return left_cnt + right_cnt + num[node]
    else:
        # 아래 2가지 경우로 나눌 수 있음
        # if left_cnt + num[node] > key and right_cnt + num[node] <= key:
        #     group += 1
        #     return right_cnt + num[node]
        # if left_cnt + num[node] <= key and right_cnt + num[node] > key:
        #     group += 1
        #     return left_cnt + num[node]
        # if left_cnt + num[node] > key and right_cnt + num[node] > key:
        #     group += 2
        #     return num[node]
        # if left_cnt + num[node] <= key and right_cnt + num[node] <= key:
        #     group += 1
        #     return min(left_cnt, right_cnt) + num[node]

        # 1. 왼쪽, 오른쪽 서브 트리 중에 하나라도 그룹화할 수 있다면
        if left_cnt + num[node] <= key or right_cnt + num[node] <= key:
            group += 1
            return min(left_cnt, right_cnt) + num[node]
        # 2. 둘다 개별 그룹으로 나눠야한다면
        else:
            group += 2
            return num[node]


def solution(k, num, links):
    global group
    parent = [-1] * len(num)
    for node, (a, b) in enumerate(links):
        if a != -1:
            parent[a] = node
        if b != -1:
            parent[b] = node
    # 부모 노드가 없는 단 하나의 노드는 루트 노드임
    root_node = parent.index(-1)

    # 각 노드를 모두 나눴을때 그룹의 개수 -> len(num)
    # 모두 나눌 수 있는 경우
    if k >= len(num):
        return max(num)

    # 최대 그룹의 최소 크기는
    # 모든 노드를 각 그룹으로 나누는 경우가 최소
    # 모든 노드가 하나의 그룹이 되는 경우(안 나누는 경우가 최대)

    # 파라메트릭 서치
    # 최대 그룹의 크기가 mid일때 그룹의 개수 group
    # group <= k
    # False, False, False, False, True, True
    # True가 되는 값 중 가장 작은 값(가장 왼쪽의 값)

    lo, hi = max(num), sum(num)
    answer = hi
    while lo < hi:
        mid = (lo + hi) // 2
        # 각 그룹의 크기가 mid이하로 유지하면서 group의 개수가 k개 이하가 될 수 있나
        group = 1
        exam_room(root_node, mid, num, links)
        if group > k:
            lo = mid + 1
        else:
            answer = mid
            hi = mid

    return answer
