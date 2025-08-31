"""
Intuition:
Given a number, its factorial can be found by multiplying all positive integers starting from 1 to the given number.

Approach:
Initialize a variable with 1 that will store the factorial of the given number.
Start iterating from 1 to the given number, and in every pass multiply the variable with the current number.
After the iterations are completed, the variable storing the answer can be returned.

Complexity Analysis:
Time Complexity: O(N) – Iterating once from 1 to N.

Space Complexity: O(1) – Using a couple of variables i.e., constant space.
"""

# Function to find the
# factorial of a number
def factorial(self, n):
    
    # Variable to store the factorial
    fact = 1

    # Iterate from 1 to n
    for i in range(1, n + 1):
        # Multiply fact with current number
        fact = fact * i
    
    # Return the factorial stored
    return fact