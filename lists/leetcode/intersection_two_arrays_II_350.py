from collections import Counter
def intersect(nums1, nums2):
    # Count elements in both arrays
    count1 = Counter(nums1)
    count2 = Counter(nums2)
    
    # Find intersection
    result = []
    for num in count1:
        if num in count2:
            # Add the minimum count of the element from both arrays
            result.extend([num] * min(count1[num], count2[num]))
    
    return result