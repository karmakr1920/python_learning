def findPoisonedDuration(timeSeries, duration):
    if not timeSeries:
        return 0

    total_poisoned_time = 0

    for i in range(len(timeSeries) - 1):
        # Time until the next attack
        gap = timeSeries[i + 1] - timeSeries[i]
        # Add either full duration, or just the gap if overlap occurs
        total_poisoned_time += min(duration, gap)

    # Last attack always contributes full duration
    total_poisoned_time += duration

    return total_poisoned_time

# print(findPoisonedDuration([1,4],2))
# Example 1:

# Input: timeSeries = [1,4], duration = 2
# Output: 4
# Explanation: Teemo's attacks on Ashe go as follows:
# - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
# - At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
# Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.
# Example 2:

# Input: timeSeries = [1,2], duration = 2
# Output: 3
# Explanation: Teemo's attacks on Ashe go as follows:
# - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
# - At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
# Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.