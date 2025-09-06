"""
Intuition
To determine the largest substring ending with an odd digit, start by iterating backward from the end of the number. This approach efficiently finds the rightmost odd digit by examining each character in reverse order. Once an odd digit is encountered, the substring from the beginning of the number up to and including this digit represents the largest possible odd-ending substring. This process leverages the fact that finding the last occurrence of an odd digit directly provides the longest valid substring.

Approach
1. Start by iterating through the string from the end towards the beginning to find the first odd digit. This digit marks the potential end of the largest odd number substring.

2. Once an odd digit is found, skip any leading zeroes from the beginning of the string up to this odd digit.

3. Extract and return the substring starting after the leading zeroes and ending at the identified odd digit. This substring represents the largest odd integer without leading zeroes.

Complexity Analysis
Time Complexity: O(N), The loop runs once through the string of length N.

Space Complexity: O(N), The auxiliary space used is O(1) but if the space for returned string is considered (which will be O(N) in the worst case), the overall space complexity comes out to be O(N).
"""

# Function to find the largest odd number 
# that is a substring of given string 
def largeOddNum(s):
    ind = -1
    
    # Step 1: Find the rightmost odd digit
    for i in range(len(s) - 1, -1, -1):
        if int(s[i]) % 2 == 1:  # odd digit found
            ind = i
            break
    
    # Step 2: If no odd digit, return ""
    if ind == -1:
        return ""
    
    # Step 3: Skip leading zeros
    i = 0
    while i <= ind and s[i] == '0':
        i += 1
    
    # Step 4: Return substring from first non-zero to odd digit
    return s[i:ind + 1]