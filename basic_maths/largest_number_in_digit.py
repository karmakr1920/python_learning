"""
Intuition:
Given a number, all the digits can be extracted from the back (right) successively and the maximum of all the digits can be found by comparing every digit.

Approach:
Initialize a variable largest digit with zero that will store the largest digit in the given number.
The last digit of the original number can be found by using the modulus operator (used to find the remainder for any division) with the number 10.
Iterate on the original number till there are digits left. In every iteration, extract the last (rightmost) digit and check if it is greater than the largest digit. If found greater, update the largest digit with the current digit.
Once the iterations are over, the largest digit in the given number is returned as answer.

Complexity Analysis:
Time Complexity: O(log10(N)) – In every iteration, N is divided by 10 (equivalent to the number of digits in N.)

Space Complexity: O(1) – Using a couple of variables i.e., constant space.
"""
# Function to find the largest
# digit in a given number
def largestDigit(n):
    # Variable to store the largest digit
    largestDigit = 0

    # Keep on iterating while there
    # are digits left to extract
    while n > 0:
        lastDigit = n % 10

        # If the current digit is greater than 
        # largest digit, update largest digit
        if lastDigit > largestDigit:
            largestDigit = lastDigit

        n = n // 10

    # Return the largest digit
    return largestDigit