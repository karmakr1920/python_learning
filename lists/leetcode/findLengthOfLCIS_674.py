def findLengthOfLCIS(nums):
    if not nums:
        return 0

    max_len = 1
    current_len = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 1  # reset the length since sequence broke

    return max_len


# Example 1:

# Input: nums = [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
# Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
# 4.
# Example 2:

# Input: nums = [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
# increasing.
 