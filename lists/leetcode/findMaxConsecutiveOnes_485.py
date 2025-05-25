def findMaxConsecutiveOnes(nums):
    # count = 0         # Current streak of 1's
    # max_count = 0     # Maximum streak found so far

    # for num in nums:
    #     if num == 1:
    #         count += 1
    #     else:
    #         # End of a streak — update max_count if needed
    #         max_count = max(max_count, count)
    #         count = 0  # Reset current streak

    # # Final check in case the array ends with 1's
    # max_count = max(max_count, count)

    # return max_count
    count = 0
    max_count = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            count+=1
        else:
            max_count = max(max_count, count)
            count = 0
    
    return max(max_count, count)


# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.