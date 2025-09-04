"""
Given a string, the task is to reverse it. The string is represented by an array of characters s. Perform the reversal in place with O(1) extra memory.

Note: no need to return anything, modify the given list.
"""

def reverseString(self, s):
    #your code goes here
    left = 0
    right = len(s) - 1
    while left < right:
        s[left],s[right] = s[right],s[left]
        left += 1
        right -= 1
    return s