"""
Approach: 
This pattern can be divided into three parts: first print the numbers, then spaces and at last numbers again.
Find out the numbers of spaces needs to printed in the first row and store it in a variable spaces.
Then iterate from 1 to N to define the number of rows. Using nested for loop print the numbers as required , then in separate loop print the spaces and finally, the numbers in third loop.
After completion of a row, decrease the number of spaces and give a line break to print next row.

Complexity Analysis: 
Time Complexity : O(N2). Where, N is the number of rows provided as an input.

Space Complexity :O(1). As no extra space is being used to print the patterns.
"""

n = 4  # example

for i in range(1, n + 1):
    # Left half
    for j in range(1, i + 1):
        print(j, end="")

    # Middle spaces
    for k in range(2 * (n - i)):
        print(" ", end="")

    # Right half
    for l in range(i, 0, -1):
        print(l, end="")

    print()
