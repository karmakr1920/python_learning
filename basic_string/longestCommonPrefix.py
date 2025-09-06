# Method to find the longest common prefix in a list of strings
def longestCommonPrefix(strs):
    # Edge case: empty list
    if not strs:
        return ""
    
    # Sort the list to get the lexicographically smallest and largest strings
    strs.sort()
    # First string (smallest in sorted order)
    first = strs[0]  
    # Last string (largest in sorted order)
    last = strs[-1]  
    
    # Compare characters of the first and last strings
    ans = []
    for i in range(min(len(first), len(last))):
        # If characters don't match, return the current prefix
        if first[i] != last[i]:
            return ''.join(ans)
        # Append the matching character to the result
        ans.append(first[i])
    
    # Return the longest common prefix found
    return ''.join(ans)


print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""

"""
Intuition
To determine the longest common prefix among a set of strings, consider the following approach: when a list of strings is sorted lexicographically, the first string and the last string in this sorted list will differ the most. The common prefix of these two strings is guaranteed to be the longest common prefix across all strings in the array. For example, if the sorted list is ["flight", "flow", "flowers", "fly"], comparing the first and last string in the sorted order gives the longest common prefix shared by all strings in the list.

Approach
Sort the array of strings.
Select the first and the last string from the sorted array. These two strings will have the maximum possible common prefix.
Initialize an index variable to zero. This index will track the length of the common prefix.
Compare characters at the current index of both selected strings. Continue moving the index forward as long as the characters at the current index are equal and the index is within the bounds of both strings.
Once characters differ or the end of one of the strings is reached, the index will indicate the length of the common prefix.
Return the substring of the first string from the start to the index, which represents the longest common prefix.

Complexity Analysis
Time Complexity: O(N * M * log N), where N is the number of strings and M is the maximum length of a string. The sorting operation takes O(N * M * log N) time, and the comparison of characters in the first and last strings takes O(M) time, which is dominated by the sorting step.

Space Complexity: O(M), as the ans variable can store the length of the prefix which in the worst case will be O(M).
"""