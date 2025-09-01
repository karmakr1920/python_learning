# Function to find all
# divisors of n
def divisors(n):
    
    # To store the divisors
    ans = []
    
    # Iterate from 1 to n
    for i in range(1, n + 1):
        
        # If a divisor is found
        if n % i == 0:
            # Add it to the answer
            ans.append(i)
    
    # Return the result
    return ans