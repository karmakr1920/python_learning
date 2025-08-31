n = 5
for i in range(1, n+1):
    start = chr(ord('A') + n - i)  # starting character
    for j in range(i):
        print(chr(ord(start) + j), end=" ")
    print()