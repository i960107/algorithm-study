from itertools import permutations


def solution(expression):
    ops = ("+", "-", "*")

    # expression을 연산과 숫자로 자르기
    arr = []
    temp = []
    for char in expression:
        if char.isdigit():
            temp.append(char)
        else:
            arr.append(int(''.join(temp)))
            temp = []
            arr.append(char)
    arr.append(int(''.join(temp)))

    def calculate(priorities, arr):
        # 우선순위 낮은 것부터 계산
        for p in range(3):
            op = priorities[p]
            temp = []
            for index, x in enumerate(arr):
                # 만약 이번 연산에 해당한다면 stack 마지막 원소를 Pop해서 계산한 값을 넣어줌
                if temp and temp[-1] == op:
                    temp.pop()
                    num = temp.pop()
                    if op == "+":
                        temp.append(num + x)
                    elif op == "-":
                        temp.append(num - x)
                    elif op == "*":
                        temp.append(num * x)
                else:
                    temp.append(x)
            arr = temp
        return arr[0]

    max_result = -float("INF")
    # 연산 우선순위
    for permutes in permutations(range(3), 3):
        priorities = {p: op for op, p in zip(ops, permutes)}
        result = calculate(priorities, arr)
        max_result = max(max_result, abs(result))

    return max_result


def solution_fail(expression):
    ops = ("+", "-", "*")

    # expression을 연산과 숫자로 자르기
    arr = []
    temp = []
    for char in expression:
        if char.isdigit():
            temp.append(char)
        else:
            arr.append(int(''.join(temp)))
            temp = []
            arr.append(char)
    arr.append(int(''.join(temp)))

    def calculate(priorities, arr):
        # 우선순위 낮은 것부터 계산
        for p in range(3):
            op = priorities[p]
            temp = []
            for index, x in enumerate(arr):
                # 틀림 none 과 == 비교할 수 없음
                # if x == None:
                if x is None:
                    continue

                if x == op:
                    first = temp.pop()
                    second = arr[index + 1]

                    if op == "+":
                        temp.append(first + second)
                    elif op == "-":
                        temp.append(first - second)
                    elif op == "*":
                        temp.append(first * second)
                    arr[index + 1] = None

                else:
                    temp.append(x)

            arr = temp
        return arr[0]

    max_result = -float("INF")
    # 연산 우선순위
    for permutes in permutations(range(3), 3):
        priorities = {p: op for op, p in zip(ops, permutes)}
        # 주의! nested function에서 nonlocal 배열 조작시 다른 case에 영향을 미치는 것 주의!
        result = calculate(priorities, arr[::])
        max_result = max(max_result, abs(result))

    return max_result


print(solution_fail("100-200*300-500+20"))
