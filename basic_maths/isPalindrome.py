"""
Intuition:
Given a number, it is a palindrome if it remains the same when its digits are reversed.

Approach:
Initialize a reversed number with zero, which will store the reversed number. Store a copy of the original number which can be used to compare the original number and reversed number.
To push any digit at the end of the reversed number, the following mathematical operation can be used: revNum = (revNum * 10) + digit.
The last digit of the original number can be found by using the modulus operator (used to find the remainder for any division) with the number 10.
Iterate on the original number till there are digits left. In every iteration, extract the last (rightmost) digit and push it at the back of the reversed number. Also, divide the original number by 10 so that the remaining digits can be extracted in the next iterations.
Once the iterations are over, the reversed number will be stored in the reverse of the original number. Check if the stored copy of the original number is the same as the reversed number. If yes, the number is palindrome else it is not a palindrome.

Complexity Analysis:
Time Complexity: O(log10(N)) – In every iteration, N is divided by 10 (equivalent to the number of digits in N.)

Space Complexity: O(1) – Using a couple of variables i.e., constant space.
"""
# Function to check if a 
# number is palindrome or not
def isPalindrome(self, n):
    # Create a copy of original number
    copy = n
    
    # After the code, revNum will
    # contain the reversed number
    revNum = 0

    # Keep on iterating while there
    # are digits left to extract
    while n > 0:
        lastDigit = n % 10

        # Pushing last digit at the
        # back of reversed number
        revNum = (revNum * 10) + lastDigit
        n = n // 10
    
    # Return true if the reversed and 
    # copy of original number is same
    return revNum == copy