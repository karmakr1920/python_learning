from collections import Counter
def longestPalindrome(words):
    counts = Counter(words)  # Count how many times each word appears
    length = 0               # Length of palindrome we build
    used_center = False      # Have we used a palindromic word in the center?

    for word in counts:
        rev = word[::-1]  # reversed word

        if word == rev:
            # Word is palindrome itself (like "ff", "oo")
            pairs = counts[word] // 2          # How many pairs we can form
            length += pairs * 4                 # Each pair adds 4 chars (2 + 2)
            if counts[word] % 2 == 1:
                used_center = True              # One leftover can go in the center
        else:
            # Word and its reverse are different, pair as many as possible
            if rev in counts:
                pairs = min(counts[word], counts[rev])
                length += pairs * 4             # Each pair adds 4 chars
                counts[rev] = 0                 # Avoid counting reverse word again

    # If we have a leftover palindromic word, add 2 for center
    if used_center:
        length += 2

    return length

# Input: words = ["lc","cl","gg"]
# Output: 6
# Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
# Note that "clgglc" is another longest palindrome that can be created.