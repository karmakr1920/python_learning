from collections import Counter
def minDeletion(s, k):
    freq = Counter(s)

    if len(freq) <= k:
        return 0

    # Get the frequencies sorted from smallest to largest
    counts = sorted(freq.values())

    # Delete the least frequent characters until only k remain
    deletions = sum(counts[:len(freq) - k])

    return deletions

print(minDeletion('aaccbb',2))