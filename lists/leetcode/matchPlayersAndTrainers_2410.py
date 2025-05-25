def matchPlayersAndTrainers(players, trainers):
    # Sort both lists to facilitate greedy matching
    players.sort()
    trainers.sort()

    # Initialize pointers for players and trainers
    p = 0  # Pointer for players
    t = 0  # Pointer for trainers
    count = 0  # Count of matched players

    # Iterate through both lists
    while p < len(players) and t < len(trainers):
        if players[p] <= trainers[t]:
            # If the trainer can handle the player, match them
            count += 1
            p += 1  # Move to next player
            t += 1  # Move to next trainer
        else:
            # Trainer too weak, try the next stronger trainer
            t += 1

    # Return the total number of successful matches
    return count


# Input: players = [4,7,9], trainers = [8,2,5,8]
# Output: 2
# Explanation:
# One of the ways we can form two matchings is as follows:
# - players[0] can be matched with trainers[0] since 4 <= 8.
# - players[1] can be matched with trainers[3] since 7 <= 8.
# It can be proven that 2 is the maximum number of matchings that can be formed.