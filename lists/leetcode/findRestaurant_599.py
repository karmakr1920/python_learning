def findRestaurant(list1, list2):
    res = []
    min_sum = float('inf')  # Initialize to infinity so any index sum will be smaller.
    
    for i in range(len(list1)):
        if list1[i] in list2:              # Check if the restaurant is common.
            j = list2.index(list1[i])      # Find its index in list2.
            idx_sum = i + j                # Calculate the index sum.
            
            if idx_sum < min_sum:          # If it's the smallest so far,
                res = [list1[i]]           # start a new result list.
                min_sum = idx_sum
            elif idx_sum == min_sum:       # If it ties with the smallest,
                res.append(list1[i])       # add to result list.
                
    return res


# Example 1:

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only common string is "Shogun".
# Example 2:

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.
# Example 3:

# Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
# Output: ["sad","happy"]
# Explanation: There are three common strings:
# "happy" with index sum = (0 + 1) = 1.
# "sad" with index sum = (1 + 0) = 1.
# "good" with index sum = (2 + 2) = 4.
# The strings with the least index sum are "sad" and "happy".