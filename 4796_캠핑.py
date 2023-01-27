import sys

vac = [[1, 1, 1]]

while vac[-1] != [0, 0, 0]:
    arr = list(map(int, sys.stdin.readline().split()))
    vac.append(arr)

length = len(vac)

for i in range(1, length-1):
    L, P, V = vac[i]
    num = 0
    moc = V // P
    rest = V % P

    num += moc * L
    if rest >= L:
        num += L
    else:
        num += rest

    print("Case " + str(i) + ": " + str(num))
