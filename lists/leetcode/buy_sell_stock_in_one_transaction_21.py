def maxProfit(prices):
    # Initialize the minimum price so far with the first day's price
    min_price = prices[0]
    # Initialize the maximum profit as 0 (no transaction yet)
    max_profit = 0

    # Start from the second day since first day's price is already used
    for price in prices[1:]:
        # If the current price is lower than the minimum seen so far, update min_price
        if price < min_price:
            min_price = price
        # Else, calculate the profit if selling today and update max_profit if it's higher
        elif price - min_price > max_profit:
            max_profit = price - min_price

    # Return the maximum profit found
    return max_profit

print(maxProfit([1,5,4,3,2,10]))