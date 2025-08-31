"""
Intuition:
Given a number, all the digits in the number can be counted by counting one by one every digit which can be done by extracting the last digit successively from the right until there are no more digits left to extract.

Approach:
Initialise a counter to keep the count of digits in the number. Keep dividing the number by 10 until no more digits are left to extract.
For every digit extracted from the number, increment the counter by 1.
Once the iterations are over, the number of digits is stored in the counter.
Edge Case:
What if the given number is zero?
Return 1, because the number of digits in zero is 1.

Complexity Analysis:
Time Complexity: O(log10(N)) – In every iteration we are dividing N by 10.

Space Complexity: O(1) – Using a couple of variables i.e., constant space.
"""

def countDigit(num):
    if num == 0:
        return 1
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count

print(countDigit(2342))