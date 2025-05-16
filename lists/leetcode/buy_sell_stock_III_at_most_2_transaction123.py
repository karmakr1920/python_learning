def maxProfit(prices):
    # if not prices:
    #     return 0

    # n = len(prices)

    # # Step 1: Calculate max profit from day 0 to i (first transaction)
    # left_profits = [0] * n
    # min_price = prices[0]
    # for i in range(1, n):
    #     min_price = min(min_price, prices[i])
    #     left_profits[i] = max(left_profits[i - 1], prices[i] - min_price)

    # # Step 2: Calculate max profit from day i to end (second transaction)
    # right_profits = [0] * n
    # max_price = prices[-1]
    # for i in range(n - 2, -1, -1):
    #     max_price = max(max_price, prices[i])
    #     right_profits[i] = max(right_profits[i + 1], max_price - prices[i])

    # # Step 3: Combine the two profits
    # max_total_profit = 0
    # for i in range(n):
    #     max_total_profit = max(max_total_profit, left_profits[i] + right_profits[i])

    # return max_total_profit
    buy1, buy2 = float('inf'), float('inf')
    sell1, sell2 = 0, 0

    for num in prices:
        buy1 = min(buy1, num)
        sell1 = max(sell1, num - buy1)
        buy2 = min(buy2, num - sell1)
        sell2 = max(sell2, num - buy2)
    
    return sell2
print(maxProfit([3,3,5,0,0,3,1,4]))