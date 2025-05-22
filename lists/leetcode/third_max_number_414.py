def thirdMax(nums):
    first = second = third = float('-inf')

    for num in nums:
        if num in (first, second, third):
            continue  # skip duplicates

        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num

    return third if third != float('-inf') else first