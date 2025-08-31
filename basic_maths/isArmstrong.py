"""
Intuition:
Given a number, the number of digits can be found. Once the number of digits is known, all the digits can be extracted one by one from the right which can be used to check whether the number is Armstrong or not.

Approach:
Initialize three variables:
count - to store the count of digits in the given number.
sum - to store the sum of the digits of the number raised to the power of the number of digits.
copy - to store the copy of the original number.
Start iterating on the given number till there are digits left to extract. In each iteration, extract the last digit (using the modulus operator with 10), and add the digit raised to the power of count to sum. Update n by integer division with 10 effectively removing the last digit.
After the iterations are over, check if the copy of the original is the same as the sum stored. If found equal, the original number is an Armstrong number, else it is not.

Complexity Analysis:
Time Complexity: O(log10(N)) – N is being divided by 10 until it becomes zero resulting in log10(N) iterations and in each iteration constant time operations are performed.

Space Complexity: O(1) – Using a couple of variables i.e., constant space, regardless of the size of the input.
"""

def isArmstrong(n):
    original = n
    power = len(str(n))   # count digits
    total = 0
    
    while n > 0:
        digit = n % 10             # get last digit
        total += digit ** power      # add digit^power to sum
        n //= 10                   # remove last digit
    
    return total == original