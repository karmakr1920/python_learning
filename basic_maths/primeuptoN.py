def isPrime(self, n):
    # Variable to store the count of divisors of n
    count = 0

    # Loop from 1 to n
    for i in range(1, n + 1):
        # Check if i is a divisor
        if n % i == 0:
            count += 1

    # If count is 2, n is prime
    if count == 2:
        return True
    return False

# Function to find count of primes till n
def primeUptoN(self, n):
    count = 0
    # Iterate from 2 to n
    for i in range(2, n + 1):
        if self.isPrime(i):
            count += 1
    return count