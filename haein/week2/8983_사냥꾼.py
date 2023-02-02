# 아이디어
# 1. 동물마다 잡힐 수 있는 사대의 최소 최대 범위를 구함
# 2. 사대의 범위 내에 사대가 있는지 이분탐색으로 탐색

m, n, l = map(int, input().split())
sade = list(map(int, input().split()))
sade.sort()
ani = []
for i in range(n):
    ani.append(list(map(int, input().split())))

cnt = 0

for a, b in ani:
    if b > l:
        continue

    min_sade = a+b-l
    max_sade = a-b+l

    # 밖에다 둬서 갱신이 안되어서 계속 틀렸음!
    start = 0
    end = len(sade) - 1

    while start <= end:
        # 사대 인덱스 (탐색하고자 하는 게 mid)
        mid = (start + end) // 2

        if min_sade <= sade[mid] <= max_sade:
            cnt += 1
            break
        elif sade[mid] < min_sade:
            start = mid + 1
        elif sade[mid] > max_sade:
            end = mid - 1

print(cnt)
