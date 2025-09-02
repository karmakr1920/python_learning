def countOdd(arr):
    # Initialize the counter for odd numbers
    odd_count = 0
    # Iterate through each element in the array
    for i in arr:
        # Check if the current element is odd
        if i % 2 == 1:
            # Increment the counter if the element is odd
            odd_count += 1
    # Return the total count of odd numbers
    return odd_count