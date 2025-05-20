def topKFrequent(nums, k):
    # Step 1: Count the frequency of each element
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Step 2: Sort elements based on their frequency in descending order
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    # Step 3: Extract the top k frequent elements
    top_k = []
    for i in range(k):
        top_k.append(sorted_freq[i][0])
    
    return top_k