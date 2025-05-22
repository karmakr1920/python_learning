def findDisappearedNumbers(nums):
    seen = set(nums)  # Hash set to store all seen numbers
    n = len(nums)

    result = []
    for i in range(1, n + 1):
        if i not in seen:
            result.append(i)

    return result
# nums = [4,3,2,7,8,2,3,1]
# seen = {1,2,3,4,7,8}
# Missing: 5,6
# Output: [5,6]
