def arraySortedOrNot(self, arr, n):
    # Iterate through the array
    for i in range(n - 1):
        
        # Compare each element with the next one
        if arr[i] > arr[i + 1]:
            
        # If any element is greater than the next one,
        # the array is not sorted  
            return False  
            
    # If no such pair is found, array is sorted
    return True  