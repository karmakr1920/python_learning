def NnumbersSum(N):
# Base case: if N is 0, return 0
    if N == 0:
        return 0
    # Recursive case: add N to the sum of N-1
    return N + NnumbersSum(N - 1)

"""
Intuition
Computing the sum of an array's elements through recursion involves thinking about adding the first element to the sum of the rest. This process continues by recursively considering one element at a time, gradually reducing the array until reaching the point where no elements are left to add.

Approach
Define a recursive helper function sum(nums, left) where nums is the array and left is the current index.
In the helper function: Base case: If the left index is out of bounds (i.e., left >= nums.length), return 0 because there are no more elements to add. Recursive case: Add the current element nums[left] to the sum of the remaining elements, obtained by recursively calling the function with the next index left + 1.
The initial call to the helper function is made from the main function with the starting index 0.

Time and Space Complexity
Time Complexity : O(N) The time complexity is O(N) because each element in the array is processed exactly once.
Space Complexity : O(N)The space complexity is O(N) due to the recursion stack, which can grow up to the size of the array.

"""