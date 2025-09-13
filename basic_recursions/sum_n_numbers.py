def NnumbersSum(N):
# Base case: if N is 0, return 0
    if N == 0:
        return 0
    # Recursive case: add N to the sum of N-1
    return N + NnumbersSum(N - 1)