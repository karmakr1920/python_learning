def maxProduct(nums):
    # Initialize max and min products ending at the first element
    max_prod = min_prod = result = nums[0]

    # Start from the second element
    for n in nums[1:]:
        # If the current number is negative, swapping helps track correct max/min
        if n < 0:
            max_prod, min_prod = min_prod, max_prod

        # max_prod is the maximum product ending at current position
        max_prod = max(n, max_prod * n)

        # min_prod is the minimum product ending at current position
        min_prod = min(n, min_prod * n)

        # Update result with the largest product seen so far
        result = max(result, max_prod)

    return result

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.