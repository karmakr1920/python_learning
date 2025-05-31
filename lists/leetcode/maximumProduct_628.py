def maximumProduct(nums):
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')

    for n in nums:
        # Find top 3 max
        if n > max1:
            max1, max2, max3 = n, max1, max2
        elif n > max2:
            max2, max3 = n, max2
        elif n > max3:
            max3 = n

        # Find bottom 2 min
        if n < min1:
            min1, min2 = n, min1
        elif n < min2:
            min2 = n

    return max(max1 * max2 * max3, min1 * min2 * max1)

# Example 1:

# Input: nums = [1,2,3]
# Output: 6
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:

# Input: nums = [-1,-2,-3]
# Output: -6