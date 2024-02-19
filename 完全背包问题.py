def fun(W, data, n):
    dp = [0] * (W + 1)
    for i in range(n):
        for w in range(data[i][0], W + 1):
            dp[w] = max(dp[w], dp[w - data[i][0]] + data[i][1])
    return dp[W]


W, n = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]  # 0为重量
print(fun(W, data, n))
