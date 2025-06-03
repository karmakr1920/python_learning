from collections import Counter
def findErrorNums(nums):
    count = Counter(nums)
    res = []
    n = len(nums)
    
    # Find the duplicated number
    for num in count:
        if count[num] == 2:
            res.append(num)
            break  # We found the duplicate, no need to continue
    
    # Find the missing number
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(set(nums))  # use set to avoid double-counting the duplicate
    missing_num = expected_sum - actual_sum
    res.append(missing_num)
    
    return res


# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]