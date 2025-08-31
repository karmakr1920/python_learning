"""
Intuition:
Given a number, it can be reversed if all the digits are extracted from the end of the original number and pushed at the back of a new reversed number.

Approach:
Initialize a reversed number with zero, which will store the reversed number. To push any digit at the end of the reversed number, the following mathematical operation can be used:
revNum = (revNum * 10) + digit.
The last digit of the original number can be found by using the modulus operator (used to find the remainder for any division) with the number 10.
Iterate on the original number till there are digits left. In every iteration, extract the last (rightmost) digit and push it at the back of the reversed number. Also, divide the original number by 10 so that the remaining digits can be extracted in the next iterations.
Once the iterations are over, the reversed number will be stored in the reverse of the original number.

Complexity Analysis:
Time Complexity: O(log10(N)) – In every iteration, N is divided by 10 (equivalent to the number of digits in N.)

Space Complexity: O(1) – Using a couple of variables i.e., constant space.
"""

def reverseNumber(n):
    res = 0
    while n > 0:
        digit = n % 10
        res = res*10 + digit
        n = n // 10
    
    return res

print(reverseNumber(354))