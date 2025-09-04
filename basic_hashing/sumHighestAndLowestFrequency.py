# Function to get the sum of highest
# and lowest frequency in array
def sumHighestAndLowestFrequency(self, nums):
    
    # Variable to store the size of array
    n = len(nums)
    
    # Variable to store maximum 
    # and minimum frequency
    maxFreq = 0
    minFreq = n
    
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
    for freq in mpp.values():
        # Update maximum and 
        # minimum frequencies
        maxFreq = max(maxFreq, freq)
        minFreq = min(minFreq, freq)
        
    # Return the required sum
    return maxFreq + minFreq