def checkPrime(num):
    if num <= 1:
        return False  # 0 and 1 are not prime numbers
    return prime(num, 2)  # Call the helper function to check for primality

def prime(num, x):
    # Base case: x > sqrt(num), so the number is prime
    if x > num ** 0.5:
        return True  
    if num % x == 0:
        # Found a divisor, so the number is not prime
        return False  
    # Recursive call with the next divisor
    return prime(num, x + 1)  

print(checkPrime(29))  # Output: True