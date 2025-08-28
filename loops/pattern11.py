"""
Approach: 
Iterate from 1 to N using a for loop, it will basically define the number of rows needed.
Now, if the row is even then start from 1, else from 0. Alternatively print 0's and 1's throughout the the current row.
Finally, print a next line at the end of a row, it ensures to print the next row as well.

Complexity Analysis: 
Time Complexity : O(N2). Where, N is the number of rows provided as an input.

Space Complexity :O(1). As no extra space is being used to print the patterns.
"""

n = 5  # you can change this

for i in range(n):
    start = 1 if i % 2 == 0 else 0
    for j in range(i + 1):
        print(start, end=" ")
        start = 1 - start   # flips between 1 and 0
    print()
