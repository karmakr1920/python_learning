# Function to find the largest odd number 
# that is a substring of given string 
def largeOddNum(self, s: str) -> str:
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