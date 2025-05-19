def maximumNum(arr):
    if not arr:
        return None  # or raise ValueError("Empty list provided")
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num
