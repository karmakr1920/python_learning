def pattern17(n):
    # Outer loop for the number of rows.
    for i in range(n):
        
        # Printing spaces before characters.
        for j in range(n - i - 1):
            print(" ", end="")
        
        # Printing characters.
        ch = 'A'
        breakpoint = (2 * i + 1) // 2
        for j in range(1, 2 * i + 2):
            print(ch, end="")
            if j <= breakpoint:
                ch = chr(ord(ch) + 1)
            else:
                ch = chr(ord(ch) - 1)
        
        # Move to the next line for the next row.
        print()

pattern17(5)