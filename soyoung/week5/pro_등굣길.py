def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    # 웅덩이는 -1로 표시
    for r, c in puddles:
        dp[c][r] = -1
    dp[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            # 웅덩이를 만나면 0으로 갱신, 현재위치의값은 왼쪽과 위의 합
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    return dp[n][m]
