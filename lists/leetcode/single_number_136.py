from collections import Counter
def singleNumber(nums):
    freq = Counter(nums)
    for num in freq:
        if freq[num] == 1:
            return num
print(singleNumber([3,3,4,2,2,3,1]))