# Function to reverse array in-place
def reverse(self, arr, n):
    left, right = 0, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # swap
        left += 1
        right -= 1