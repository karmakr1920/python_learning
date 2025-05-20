# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
from collections import Counter
def containsDuplicate(nums):
    freq = Counter(nums)
    for count in freq.values():
        if count >= 2:
            return True
    return False