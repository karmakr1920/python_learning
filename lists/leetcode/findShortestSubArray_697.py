from collections import Counter

def findShortestSubArray(nums):
    counts = Counter(nums)
    degree = max(counts.values())
    
    first = {}
    last = {}
    
    for i, num in enumerate(nums):
        if num not in first:
            first[num] = i
        last[num] = i  # always update last position

    min_len = len(nums)

    for num in counts:
        if counts[num] == degree:
            min_len = min(min_len, last[num] - first[num] + 1)

    return min_len


# Example 1:

# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:

# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.