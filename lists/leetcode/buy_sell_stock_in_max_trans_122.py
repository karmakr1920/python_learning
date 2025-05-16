# Stock Buy and Sell – Multiple Transactions Allowed
def maximumProfit(prices):
    # Initialize profit to 0
    profit = 0

    # Traverse through the price list starting from the second day
    for i in range(1, len(prices)):
        # If today's price is higher than yesterday's, it's profitable to sell today
        if prices[i] > prices[i - 1]:
            # Add the profit from this transaction
            profit += prices[i] - prices[i - 1]
    
    # Return the total profit from all profitable transactions
    return profit

# Test the function with a sample input
print(maximumProfit([100, 180, 20, 300, 340, 20]))
