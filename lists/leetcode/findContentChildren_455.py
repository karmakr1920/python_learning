def findContentChildren(g, s):
    # g.sort()
    # s.sort()
    # child = 0
    # cookie = 0

    # while child < len(g) and cookie < len(s):
    #     if s[cookie] >= g[child]:
    #         # Cookie satisfies the child
    #         child += 1
    #     cookie += 1

    # return child
    g.sort()
    s.sort()
    
    child = 0  # Pointer to current child

    for cookie in s:
        if child == len(g):
            break  # All children are satisfied
        if cookie >= g[child]:
            child += 1  # Give this cookie to the current child

    return child

# Input: g = [1,2,3], s = [1,1]
# Output: 1
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
# And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
# You need to output 1.