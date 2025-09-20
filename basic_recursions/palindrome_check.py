def palindromeCheck(s):
        # Call the recursive helper method with initial indices
        return isPalindrome(s, 0, len(s) - 1)
    
def isPalindrome(s, left, right):
    # Base Case: If the start index is greater than or equal to the end index
    if left >= right:
        return True
    # Check if characters at the current positions are the same
    if s[left] != s[right]:
        return False  # Characters do not match, so it's not a palindrome
    # Recur for the next set of characters
    return isPalindrome(s, left + 1, right - 1)

print(palindromeCheck("racecar"))  # Output: True