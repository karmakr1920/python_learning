"""
Approach: 
Use nested for loops to print the pattern. First, figure out what is the total number of rows for which the pattern needs to be printed.
Then, print the asterisks incrementally till half the total number of rows and after that decrease the asterisks according to the row number.

Complexity Analysis: 
Time Complexity : O(N2). Where N is the input provided. This quadratic complexity arises due to the nested loops iterating over N rows and printing a number of stars that sums up to approximately N2 stars in total.

Space Complexity :O(1). As no extra space is being used to print the patterns.

"""

n = int(input())
for i in range(1,n + 1):
    for j in range(1, i + 1 ):
        print("*",end="")
    print()
for i in range(n,1,-1):
    for j in range(1, i):
        print("*",end="")
    print()

