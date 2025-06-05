def dominantIndex(nums):
    if not nums:
        return -1

    max_num = max(nums)
    max_index = nums.index(max_num)

    for i, num in enumerate(nums):
        if i != max_index and max_num < 2 * num:
            return -1

    return max_index


# Example 1:

# Input: nums = [3,6,1,0]
# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: -1
# Explanation: 4 is less than twice the value of 3, so we return -1.