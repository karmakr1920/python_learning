def canPlaceFlowers(flowerbed, n):
    length = len(flowerbed)
    
    for i in range(length):
        if flowerbed[i] == 0:
            empty_left = (i == 0) or (flowerbed[i - 1] == 0)
            empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)
            
            if empty_left and empty_right:
                flowerbed[i] = 1  # Place flower
                n -= 1
                if n == 0:
                    return True
                    
    return n <= 0

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false