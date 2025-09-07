def isIsomorphic(s: str, t: str) -> bool:
    # Step 1: If lengths are different, they can never be isomorphic
    if len(s) != len(t):
        return False

    # Step 2: Create two dictionaries (hash maps)
    # One for mapping characters from s → t
    # Another for mapping characters from t → s
    map_s_t = {}
    map_t_s = {}

    # Step 3: Loop through characters of both strings by index
    for i in range(len(s)):
        char_s = s[i]  # character from s
        char_t = t[i]  # corresponding character from t

        # Step 4: Check if char_s already has a mapping
        if char_s in map_s_t:
            # If it does, and it doesn’t match the current char_t, not isomorphic
            if map_s_t[char_s] != char_t:
                return False
        else:
            # If it doesn’t exist yet, create the mapping s → t
            map_s_t[char_s] = char_t

        # Step 5: Check the reverse mapping (t → s)
        if char_t in map_t_s:
            # If it exists but doesn’t map back to char_s, not isomorphic
            if map_t_s[char_t] != char_s:
                return False
        else:
            # Otherwise, create the mapping t → s
            map_t_s[char_t] = char_s

    # Step 6: If we finish the loop without conflicts, strings are isomorphic
    return True


"""
Intuition:
To determine if two strings are isomorphic, the key insight is to recognize that two strings are isomorphic if the characters in one string can be replaced to get the other string. This can be efficiently checked by ensuring that there is a consistent mapping of characters from the first string to the second string and vice versa. The challenge lies in maintaining this mapping as the strings are traversed, ensuring that each character in the first string maps uniquely to a character in the second string, and that no two characters in the first string map to the same character in the second string.

Approach:
Initialize two arrays of size 256 (to cover all ASCII characters) to store the last seen positions of characters in both strings. This helps in tracking the mapping between characters.
Iterate through each character in the strings simultaneously. For each character, compare the last seen positions stored in the arrays. If the positions do not match, it indicates an inconsistent mapping, and the strings are not isomorphic.
If the positions match, update the arrays with the current index (incremented by 1 to avoid the default value of 0). This ensures that the mapping is consistent throughout the strings.
After completing the iteration, if no inconsistencies in the mappings are found, the strings are confirmed to be isomorphic. If any inconsistency is found during the iteration, return false immediately.

Complexity Analysis:
Time Complexity: O(N) where N is the length of the input strings, due to the single loop iterating through each character

Space Complexity: O(k) O(1) since the space used by the arrays is constant (256 fixed size) regardless of input size
"""