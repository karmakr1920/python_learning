def mostFrequentEven(nums):
    freq = {}
    for num in nums:
        if num % 2 == 0:
            freq[num] = freq.get(num, 0) + 1

    if not freq:
        return -1

    # Find the maximum frequency
    max_freq = max(freq.values())

    # Filter numbers with max frequency and return the smallest one
    candidates = [num for num, count in freq.items() if count == max_freq]
    return min(candidates)