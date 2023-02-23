n = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(n)]  # 각 인덱스 번호가 가장 끝에 들어간 부분 수열의 최대 길이

for i in range(n):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
