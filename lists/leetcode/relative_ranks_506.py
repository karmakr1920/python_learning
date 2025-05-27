def findRelativeRanks(score):
    # Create a list of (score, index) pairs
    score_with_index = [(s, i) for i, s in enumerate(score)]
    
    # Sort the list in descending order of scores
    score_with_index.sort(reverse=True)

    # Prepare the result list with empty strings
    result = [''] * len(score)

    # Define the top 3 medals
    medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]

    # Assign ranks
    for rank, (s, i) in enumerate(score_with_index):
        if rank < 3:
            result[i] = medals[rank]
        else:
            result[i] = str(rank + 1)

    return result



# Input: score = [5,4,3,2,1]
# Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].