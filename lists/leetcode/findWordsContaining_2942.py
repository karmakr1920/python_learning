def find_indices_with_char(words, x):
    result = []
    for index, word in enumerate(words):
        if x in word:
            result.append(index)
    return result

# Input: words = ["leet","code"], x = "e"
# Output: [0,1]
# Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.