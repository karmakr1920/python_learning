def longestCommonPrefix(strs):
    if not strs:
        return ""

    for i in range(len(strs[0])):  # Loop over characters in first word
        char = strs[0][i]
        for word in strs[1:]:
            if i >= len(word) or word[i] != char:
                return strs[0][:i]  # Found mismatch
    return strs[0]
