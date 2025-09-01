def LCM(n1, n2):
    # Variable to store lcm
    lcm = 0
    
    # Variable to store max of n1 & n2
    n = max(n1, n2)
    i = 1
    
    while True:
        # Variable to store multiple
        mul = n * i
        
        # Checking if multiple is common
        # common for both n1 and n2
        if mul % n1 == 0 and mul % n2 == 0:
            lcm = mul
            break
        i += 1
    
    # Return the stored LCM
    return lcm