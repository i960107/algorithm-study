N, L = map(int, input().split())
arr = list(map(int, input().split()))
sorted_arr = sorted(arr)

stk = [sorted_arr.pop()] # 기준
num = 1

while len(sorted_arr) > 0:
    if stk[-1] + 0.5 - L <= sorted_arr[-1] - 0.5:
        # 기준은 변하지 않음 (아직 테이프 한 개가 충족 가능한 상태)
        sorted_arr.pop()
    else:
        stk.append(sorted_arr.pop())
        num += 1

print(num)
