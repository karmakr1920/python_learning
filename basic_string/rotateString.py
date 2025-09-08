class Solution:
# Strings must be of the same length to be rotations of each other
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False  
        doubled_s = s + s  # Concatenate s with itself
        return goal in doubled_s  # Check if goal is a substring of s + s

# Test cases
sol = Solution()
print(sol.rotateString("abcde", "cdeab")) 
print(sol.rotateString("abcde", "abced")) 
