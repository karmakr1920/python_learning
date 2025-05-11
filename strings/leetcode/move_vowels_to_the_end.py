# Statement:
# Given a list of lowercase characters, move all the vowels to the end of the list in-place. Maintain the relative order of consonants and vowels.

def move_vowels_to_the_end(s):
    vowels = set("aeiou")
    n = len(s)
    index = 0  # Pointer to place consonants

    # Step 1: Move all consonants to the front in their original order
    for i in range(n):
        if s[i] not in vowels:
            s[index] = s[i]
            index += 1

    # Step 2: Add vowels after consonants in their original order
    for i in range(n):
        if s[i] in vowels:
            s[index] = s[i]
            index += 1

    return s


print(move_vowels_to_the_end(['a', 'b', 'c', 'e', 'f', 'i', 'o', 'u', 'd']))
