n = int(input())
for i in range(n):
            
    #This loop will print the spaces
    for j in range( (n-i-1)):
        print(" ",end="")
    
    # This loop will print asterisk.
    for j in range(2*i+1):
        print("*", end="")

    """ As soon as n stars are printed, move
    to the next row and give a line break."""
    print()

for i in range(n, 0, -1):          # rows: n → 1
    for j in range(0, n-i):        # spaces: increase each row
        print(" ", end="")
    for j in range(0, 2*i-1):      # stars: decrease each row
        print("*", end="")
    print()