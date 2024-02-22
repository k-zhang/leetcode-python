def min_cost_climbing_stairs(cost):
    cost_len = len(cost)
    if cost_len in [0, 1]:
        return 0

    dp = [0 for _ in range(cost_len + 1)]
    dp[1] = cost[0]

    for i in range(2, cost_len + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 1])

    return min(dp[cost_len], dp[cost_len - 1])
