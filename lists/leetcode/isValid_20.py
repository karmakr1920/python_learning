def isValid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map.values():  # opening brackets
            stack.append(char)
        elif char in bracket_map:         # closing brackets
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:
            return False  # in case of unexpected characters
    
    return not stack


# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true