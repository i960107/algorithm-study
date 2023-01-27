from collections import deque
N, K = map(int, input().split())
arr = list(map(int, input().split()))
used = deque(arr)

# 콘센트
consent = []
# 전자제품 : 남은 횟수
cnt = {}
for i in arr:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
# 답
ans = 0

for i in arr:
    print(i)
    print(used)
    print(consent)
    print(cnt)
    print("=====")
    if len(consent) < N:
        if i not in consent:
            consent.append(i)
            # cnt[i] -= 1
            # used.popleft()
    else:
        if i not in consent:
            for k in consent:
                if cnt[k] == 0:
                    ans += 1
                    # cnt[i] -= 1
                    consent.remove(k)
                    # used.popleft()
                    consent.append(i)
            else:
                tmp = list(used)
                remove = 0
                pop = 0
                for j in consent:
                    if remove < tmp.index(j):
                        pop = j # 제거할 전자제품 번호
                        remove = tmp.index(j) # 전자제품의 인덱스
                ans += 1
                # cnt[i] -= 1
                consent.remove(pop)
                # used.popleft()
                consent.append(i)
    cnt[i] -= 1
    used.popleft()

print(ans)




