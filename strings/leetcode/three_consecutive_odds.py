def three_consecutive_odds(arr):
    count = 0  # Tracks consecutive odd numbers

    for num in arr:
        if num % 2 == 1:      # If the number is odd
            count += 1
            if count == 3:    # Found 3 in a row
                return True
        else:
            count = 0         # Reset count if the number is even

    return False
