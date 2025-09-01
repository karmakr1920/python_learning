"""
Intuition:
Given a number, all its proper divisors (divisors that divide the number without leaving any remainder, excluding the number itself) can be found and summed up. Then, the sum can be compared with the number itself. If the sum is the same as the number, then it is a perfect number, otherwise, it is not.

Approach:
Initialize a variable with 0 to store the sum of the proper divisors.
Start iterating from 1 to the given number(excluding) using a loop variable, and check whether the number is divisible completely (leaving the remainder zero) by the loop variable.
If it is divisible completely, the current value of the loop variable is a proper divisor which is added to the sum storing sum of proper divisors.
After the sum is calculated, compare it with the given number. If found equal, the given number is perfect, otherwise, it is not.

Complexity Analysis:
Time Complexity: O(N) – Running a loop from 1 to N.

Space Complexity: O(1) – Using a couple of variables i.e., constant space, regardless of the size of input.
"""

# Function to find whether the
# number is perfect or not
def isPerfect(self, n):
    
    # Variable to store the sum
    # of all proper divisors
    sum = 0
    
    # Loop from 1 to n
    for i in range(1, n):
        
        # Check if i is a proper divisor
        if n % i == 0:
            # Update sum
            sum = sum + i
    
    # Compare sum and n
    return sum == n