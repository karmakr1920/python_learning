"""
Approach: 
Use a for loop to iterate from 0 to N-1, where N is the number of rows. This loop will ensure to print each row of the pattern.
The inner loop will run for i times and print alphabets from 'A' to 'A' + (row number).
After completing a row give a line break, to make sure next row gets printed as well.

Complexity Analysis: 
Time Complexity : O(N2). The overall complexity will be O(N2), where N is the number of rows.

Space Complexity :O(1). As no extra space is being used to print the patterns.
"""
n = 5

for i in range(n):
    for j in range(i + 1):
        print(chr(ord('A') + j), end="")
    print()
