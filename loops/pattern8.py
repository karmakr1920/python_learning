"""
Approach:
Iterate from 0 to N-1 using a loop, where N is the number of rows. This loop will ensure to print each row of the pattern.
Now, run another loop from 0 to the current value of outer loop variable. It will basically print the spaces before asterisks as required in every row.
Again, run a loop, print the asterisk, all in one line, to complete the current row.
Move to a new line after printing each row to maintain the right-angled triangle shape of the pattern.


Complexity Analysis: 
Time Complexity : O(N2). As the outer loop runs for N times and the first inner loop runs for(0 + 1 + 2 + .. + N-1), the second inner loop runs in decreasing manner in each iteration((2*N -1) + (2*N - 3) + ... + 1) . So, overall it is O(N2).

Space Complexity :O(1). As no extra space is being used to print the patterns.
"""

n = int(input())
for i in range(n, 0, -1):          # rows: n → 1
    for j in range(0, n-i):        # spaces: increase each row
        print(" ", end="")
    for j in range(0, 2*i-1):      # stars: decrease each row
        print("*", end="")
    print()
