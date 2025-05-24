def summaryRanges(nums):
    result = []
    if not nums:
        return result

    start = nums[0]

    for i in range(1, len(nums)):
        # If current number is not consecutive
        if nums[i] != nums[i - 1] + 1:
            end = nums[i - 1]
            # Add the range to result
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}->{end}")
            start = nums[i]  # Start a new range

    # Add the final range
    if start == nums[-1]:
        result.append(str(start))
    else:
        result.append(f"{start}->{nums[-1]}")

    return result
