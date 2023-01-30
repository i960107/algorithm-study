N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 콘센트
consent = []
# 답
ans = 0

# 멀티탭에 이미 해당 제품 있을 경우 -> pass
# 멀티탭에 빈 구멍 있을 경우 -> 꽂아주면 됨
# 멀티탭에 빈 구멍 없을 경우
# 1. 멀티탭에 꽂혀있는 제품 중 이후로 사용되는 게 없는 경우 -> 사용되지 않는 것 뽑고 새로운 거 꽂아주면 됨
# 2. 멀티탭에 꽂혀있는 제품이 이후에도 사용되는 경우 -> 꽂혀있는 제품 중 가장 나중에 사용되는 거 뽑고 새로운 거 꼽아주면 됨

for i in range(len(arr)):
    if arr[i] in consent:
        continue
    else:
        if len(consent) < N:
            consent.append(arr[i])
        else:
            tmp = arr[i:]
            for c in consent:
                if tmp.count(c) == 0: # 이후에 사용되지 않는 게 있을 때
                    consent.remove(c)
                    ans += 1
                    break
            else: # 이후에 다 사용될 때
                ind = -1
                big = 0
                for j in consent:
                    if ind < tmp.index(j):
                        big = j
                        ind = tmp.index(j)
                consent.remove(big)
                ans += 1
            consent.append(arr[i])

print(ans)
