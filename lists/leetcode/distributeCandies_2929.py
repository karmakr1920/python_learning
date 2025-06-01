def distributeCandies(n, limit):
    # Total number of integer solutions (a + b + c = n)
    def total_ways(s):
        if s < 0:
            return 0
        return (s + 2) * (s + 1) // 2  # combinations with repetition: C(s+2, 2)

    total = total_ways(n)

    # Subtract cases where someone gets more than limit using Inclusion-Exclusion
    total -= 3 * total_ways(n - (limit + 1))      # One child gets > limit
    total += 3 * total_ways(n - 2 * (limit + 1))  # Two children get > limit
    total -= total_ways(n - 3 * (limit + 1))      # All three get > limit

    return total
    # count = 0
    # for a in range(0, min(n, limit) + 1):
    #     for b in range(0, min(n - a, limit) + 1):
    #         c = n - a - b
    #         if 0 <= c <= limit:
    #             count += 1
    # return count
    # total = 0
    # # a is the candies given to the first child.
    # for a in range(0, limit + 1):
    #     # The remaining candies for b and c.
    #     remaining = n - a
        
    #     # We need to distribute 'remaining' candies to children b and c.
    #     # Each can get at most 'limit' candies and at least 0.
    #     # For a given value b, child c gets: c = remaining - b.
    #     #
    #     # Conditions for b and c to be valid:
    #     #   0 <= b <= limit
    #     #   0 <= c = remaining - b <= limit
    #     #
    #     # The condition for c gives:
    #     #   remaining - limit <= b <= remaining
        
    #     # Combining both b constraints:
    #     b_min = max(0, remaining - limit)
    #     b_max = min(limit, remaining)
        
    #     # If b_min <= b_max, the count of valid pairs (b, c) is:
    #     if b_min <= b_max:
    #         total += (b_max - b_min + 1)
    
    # return total

# Example 1:

# Input: n = 5, limit = 2
# Output: 3
# Explanation: There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).
# Example 2:

# Input: n = 3, limit = 3
# Output: 10
# Explanation: There are 10 ways to distribute 3 candies such that no child gets more than 3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0) and (3, 0, 0).