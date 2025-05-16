def maxSubArray(arr):
    current = -1
    max_sum = arr[0]
    for num in arr:
        if current < 0:
            current = num
        else:
            current += num
        max_sum = max(current,max_sum)
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))