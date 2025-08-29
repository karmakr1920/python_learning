def pattern(n):
    for i in range(1, n+1):                     # row loop
        start = chr(ord('A') + n - i)           # starting letter
        for j in range(i):                      # print i letters
            print(chr(ord(start) + j), end=" ") # next letters
        print()                                 # new line
pattern(5)