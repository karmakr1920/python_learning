def reverseString(s):
    #your code goes here
    def reverse(s, left, right):
        # Base case
        if left >= right:
            return 
        
        # Swap characters at left and right positions
        s[left], s[right] = s[right], s[left]
        
        # Recursive call with updated indices
        reverse(s, left + 1, right - 1)
    
    reverse(s, 0, len(s) - 1)
    return s