"""
Approach: 
Iterate from 0 to N-1, where N is the number of rows. This loop will ensure to print each row of the pattern.
Now, run another loop from 0 to the current value of outer loop variable. It will basically print the spaces before asterisks as required in every row.
Again, run a loop, print the asterisk, all in one line, to complete the current row.
Move to a new line after printing each row to maintain the right-angled triangle shape of the pattern.

Complexity Analysis: 
Time Complexity : O(N2). As the outer loop runs for N times and the first inner loop runs for(N-1 + N-2 + ... + 1), the second inner loop runs incrementally in each iteration(1 + 3 + 5 + ...+2* N-1). So, overall it is O(N2).

Space Complexity :O(1). As no extra space is being used to print the patterns.
"""

n = int(input())
for i in range(0,n):
            
    #This loop will print the spaces
    for j in range(0, (n-i-1)):
        print(" ",end="")
    
    # This loop will print asterisk.
    for j in range(0,2*i+1):
        print("*", end="")

    """ As soon as n stars are printed, move
    to the next row and give a line break."""
    print()