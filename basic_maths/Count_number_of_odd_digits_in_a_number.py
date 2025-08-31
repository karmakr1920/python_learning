"""
Intuition:
Given a number, all the digits in the number can be extracted one by one from right to left which can be checked for even and odd.

Approach:
The last digit of the given number can be found by using the modulus operator (used to find the remainder for any division) with the number 10.
Iterate on the original number till there are digits left, extract the last (rightmost) digit, and check whether the digit is odd or not. In every iteration, divide the original number by 10 so that the remaining digits can be extracted in the next iterations.
Keep a counter to count the number of odd digits found in the number and every time an odd digit is encountered, increment the counter.

Complexity Analysis:
Time Complexity: O(log10(N)) – In every iteration we are dividing N by 10 (equivalent to the number of digits in N).

Space Complexity: O(1) – Using only couple of variables i.e., constant space.
"""

def countOddDigit(num):
    oddigit = 0
    while num > 0:
        digit = num % 10
        if digit % 2 != 0:
            oddigit += 1
        num //= 10
    return oddigit

print(countOddDigit(42332))