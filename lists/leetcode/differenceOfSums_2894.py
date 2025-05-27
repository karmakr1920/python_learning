def differenceOfSums(n, m):
    sum1 = 0
    sum2 = 0
    for i in range(1, n + 1):
        if i % m == 0:
            sum2 += i
        else:
            sum1 += i
    return sum1 - sum2


# Input: n = 10, m = 3
# Output: 19
# Explanation: In the given example:
# - Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], num1 is the sum of those integers = 37.
# - Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is the sum of those integers = 18.
# We return 37 - 18 = 19 as the answer.
