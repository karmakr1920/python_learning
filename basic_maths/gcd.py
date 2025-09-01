def GCD(n1, n2):
    # Variable to store the gcd
    gcd = 1
    
    # Iterate from 1 to min(n1, n2)
    for i in range(1, min(n1, n2) + 1):
        
        # Check if i is a common
        # divisor of both n1 and n2
        if n1 % i == 0 and n2 % i == 0:
            
            # Update gcd
            gcd = i
    
    # Return stored GCD.
    return gcd