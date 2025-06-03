def findDuplicate(nums):
    # Phase 1: Detect intersection
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Phase 2: Find entrance to the cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow
    # left = 1
        # right = len(nums) - 1  # range is [1, n]

        # while left < right:
        #     mid = (left + right) // 2
        #     count = sum(num <= mid for num in nums)

        #     if count > mid:
        #         right = mid
        #     else:
        #         left = mid + 1

        # return left
        # freq={}
        # for num in nums:
        #     if num not in freq:
        #         freq[num] = 0
        #     freq[num] += 1
        # for num in freq:
        #     if freq.get(num)>1:
        #         return num

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3