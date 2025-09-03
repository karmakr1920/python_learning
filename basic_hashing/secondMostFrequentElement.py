# Function to get the second highest 
# occurring element in array
def secondMostFrequentElement(self, nums):
    
    # Step 1: Build frequency dictionary manually
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Step 2: If only one unique element → no second most
    if len(freq) < 2:
        return -1

    # Step 3: Find highest and second highest frequencies
    maxFreq = 0
    secMaxFreq = 0
    maxEle = -1
    secEle = -1

    for ele, count in freq.items():
        if count > maxFreq:
            # Shift current max down to second
            secMaxFreq = maxFreq
            secEle = maxEle
            maxFreq = count
            maxEle = ele
        elif count == maxFreq:
            # Tie for highest → take smaller element
            if ele < maxEle:
                maxEle = ele
        elif count > secMaxFreq:
            secMaxFreq = count
            secEle = ele
        elif count == secMaxFreq:
            # Tie for second highest → take smaller element
            if secEle == -1 or ele < secEle:
                secEle = ele

    # Step 4: Return result (or -1 if none)
    if secEle == -1:
        return -1
    return secEle