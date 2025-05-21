# Python Program to move all zeros to end using one traversal

# Function which pushes all zeros to end of array
def pushZerosToEnd(arr):
    # Pointer to track the position for next non-zero element
    count = 0
    for i in range(len(arr)):
        # If the current element is non-zero
        if arr[i] != 0:
            # Swap the current element with the 0 at index 'count'
            arr[i],arr[count] = arr[count],arr[i]
            # Move 'count' pointer to the next position
            count += 1
    return arr

#sample test case
# print(pushZerosToEnd([1,2,0,4,0,4,0]))