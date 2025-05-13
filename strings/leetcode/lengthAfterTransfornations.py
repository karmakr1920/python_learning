def lengthAfterTransformations(s,t):
    MOD = 10**9 + 7  # To avoid large numbers, take result modulo 1e9 + 7

    # Initialize character count array for 'a' to 'z'
    curr = [0] * 26

    # Count the frequency of each character in the initial string
    for ch in s:
        index = ord(ch) - ord('a')  # Convert character to index (0 for 'a', ..., 25 for 'z')
        curr[index] += 1

    # Perform the transformation t times
    for _ in range(t):
        next_count = [0] * 26  # New frequency array for the next step

        for i in range(26):
            if i == 25:
                # If the character is 'z', it turns into 'a' + 'b'
                next_count[0] = (next_count[0] + curr[i]) % MOD  # 'a'
                next_count[1] = (next_count[1] + curr[i]) % MOD  # 'b'
            else:
                # All other characters just move to the next character in the alphabet
                next_count[i + 1] = (next_count[i + 1] + curr[i]) % MOD

        curr = next_count  # Update current frequency for next iteration

    # Calculate the total number of characters after t transformations
    total_length = 0
    for count in curr:
        total_length = (total_length + count) % MOD

    return total_length

# print(lengthAfterTransformations('acabcdzez',2))