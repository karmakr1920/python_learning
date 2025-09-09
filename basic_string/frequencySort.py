def frequencySort(self, s):
    # Step 1: Count characters manually
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Step 2: Sort by frequency (descending), then alphabetically
    sorted_chars = sorted(freq.keys(), key=lambda x: (-freq[x], x))

    return sorted_chars