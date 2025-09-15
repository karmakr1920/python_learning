def factorial(n):
    #Your code goes here
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)