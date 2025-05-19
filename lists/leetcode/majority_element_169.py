from collections import Counter
def majorityElement(nums):
    freq = Counter(nums)
    n = len(nums)
    for num, count in freq.items():
        if count > n // 2:
            return num