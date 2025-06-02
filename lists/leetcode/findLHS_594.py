from collections import Counter
def findLHS(nums):
    freq = Counter(nums)
    max_length = 0

    for num in freq:
        if num + 1 in freq:
            max_length = max(max_length, freq[num] + freq[num + 1])
    
    return max_length
    # nums.sort()
    # left = 0
    # max_len = 0

    # for right in range(len(nums)):
    #     while nums[right] - nums[left] > 1:
    #         left += 1
    #     if nums[right] - nums[left] == 1:
    #         max_len = max(max_len, right - left + 1)
    
    # return max_len


# Example 1:

# Input: nums = [1,3,2,2,5,2,3,7]

# Output: 5

# Explanation:

# The longest harmonious subsequence is [3,2,2,2,3].

# Example 2:

# Input: nums = [1,2,3,4]

# Output: 2

# Explanation:

# The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

# Example 3:

# Input: nums = [1,1,1,1]

# Output: 0

# Explanation:

# No harmonic subsequence exists.