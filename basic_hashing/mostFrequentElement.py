# Function to get the highest
# occurring element in array n
def mostFrequentElement(self, nums):
    
    # Variable to store the size of array
    n = len(nums)
    
    # Variable to store maximum frequency
    maxFreq = 0
    
    # Variable to store element
    # with maximum frequency
    maxEle = 0
    
    # HashMap
    mpp = {}
    
    # Iterating on the array
    for num in nums:
        # Updating hashmap
        if num in mpp:
            mpp[num] += 1
        else:
            mpp[num] = 1
    
    # Iterate on the map
    for ele, freq in mpp.items():
        if freq > maxFreq:
            maxFreq = freq
            maxEle = ele
        elif freq == maxFreq:
            maxEle = min(maxEle, ele)
    
    # Return the result
    return maxEle