def findWords(words):
    # Define the three keyboard rows as sets
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")

    valid_words = []

    for word in words:
        letters = set(word.lower())  # Case-insensitive check using lowercase

        # Check if all letters of the word are in one row
        if letters.issubset(row1) or letters.issubset(row2) or letters.issubset(row3):
            valid_words.append(word)

    return valid_words


# Input: words = ["Hello","Alaska","Dad","Peace"]

# Output: ["Alaska","Dad"]

# Explanation:

# Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.
