# Beginner Level
# Create a list of even numbers from 1 to 20.
even_num_list = [x for x in range(1,21) if x%2 == 0]
print(f"List of even numbers :{even_num_list}")

# Find the largest number in a list.
given_list = [2,4,43,234,5,5,3,2,12,2]
largest = given_list[0]
for i in range(len(given_list)):
    if given_list[i] > largest:
        largest = given_list[i]
print(f"Largest number in the Given List : {largest}")


# Count how many times a specific element appears in a list.
# Example
target = 2
count = 0

for i in given_list:
    if i == target:
        count += 1

print(f"Count of 2 : {count}")  # Output: 3

# Remove all occurrences of a specific element from a list.
for i in given_list:
    if target in given_list:
        given_list.remove(target)
print(f"After removal of specific target element {given_list}")
# Reverse a list without using .reverse() or slicing.
def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        # Swap elements
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

    return lst

# Example
nums = [1, 2, 3, 4, 5]
print(reverse_list(nums))  # Output: [5, 4, 3, 2, 1]

# Get the second-largest element in a list.
def second_largest(nums):
    if len(nums) < 2:
        return None

    first = second = float('-inf')

    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second if second != float('-inf') else None

# Example
print(second_largest([10, 20, 4, 45, 99]))  # Output: 45

# Flatten a 2D list into a 1D list.
def flatten_2d_list(matrix):
    result = []
    for row in matrix:
        for item in row:
            result.append(item)
    return result

# Example
matrix = [[1, 2], [3, 4], [5, 6]]
print(flatten_2d_list(matrix))  # Output: [1, 2, 3, 4, 5, 6]
