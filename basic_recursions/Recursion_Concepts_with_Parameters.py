"""
Parameterized Recursion
In basic recursion, global variables or implicit logic are sometimes used to control the recursion state. Parameterized recursion involves passing all required information as parameters to the recursive function. This approach results in:

Better control over recursion flow
Cleaner and more maintainable code
Independence from external or global state

Now, let's understand parameterized recursion with the help of a few examples.

Example 1: Print Value X, N Times
Problem: Given two numbers X and N, print the value X exactly N times using recursion.

Recursive Approach With Parameters

"""
def print_x_n_times(x, n):
    if n == 0:
        return  # base case
    print(x, end=" ")  # print the value
    print_x_n_times(x, n - 1)  # recursive call with reduced n

if __name__ == "__main__":
    x = 4
    n = 5

    # Printing X, N number of times
    print_x_n_times(x, n)


"""
Explanation: Each recursive call prints the value x once and decreases n by 1 until n reaches zero, which terminates recursion.
Example 2: Print Numbers from 1 to N
Problem: Given a number N, print all the numbers from 1 to N.

To solve this problem, both head and tail recursion work.

Head Recursion (Work Happens After Recursion)

"""
# Recursive function to print numbers from 1 to N
def print_1_to_n(i, n):
    if i > n:
        return
    print_1_to_n(i + 1, n)  # recursive call before printing
    print(i, end=" ")        # print after recursion call

if __name__ == "__main__":
    n = 5
    # Printing 1 to N
    print_1_to_n(1, n)

# Tail Recursion (Work Happens Before Recursion)
# Recursive function to print numbers from 1 to N
def print_1_to_n(i, n):
    if i > n:
        return
    print(i, end=" ")            # print before recursion call
    print_1_to_n(i + 1, n)       # recursive call after printing

if __name__ == "__main__":
    n = 5
    # Printing 1 to N
    print_1_to_n(1, n)


# Printing 1 to N Using Single Parameter
# Recursive function to print numbers from 1 to N
def print1ToN(n):
    if n == 0:
        return
    print1ToN(n - 1)           # recursive call after printing
    print(n, end=" ")          # print after recursion call

n = 5

# Printing 1 to N
print1ToN(n)

"""
Explanation: Each recursive call decreases the value of N and calls the function recursively with the updated value until it reaches 0. On the return path, each call prints the value N until the first call made is returned.
Example 3: Print Numbers from N to 1
Printing the numbers from N to 1 is similar to printing the numbers from 1 to N.

While printing the numbers from 1 to N, head recursion was used (where work happens after the recursion call). This had printed the numbers in the order from 1 to N.

Now, in order to print the numbers from N to 1, tail recursion can be used. In the tail recursion, work (printing the number) happens before the recursion call. This will print the numbers in decreasing order from N to 1.
"""
# Recursive function to print numbers from N to 1
def printNto1(n):
    if n == 0:
        return
    print(n, end=" ")          # print before recursion call
    printNto1(n - 1)           # recursive call after printing

n = 5

# Printing N to 1

printNto1(n)

"""
Explanation: Each recursive call prints the value of N and decreases the value of N by 1 and calls recursively the function with the updated value until it reaches 0. This prints the numbers from N to 1.

If we wish to use Head recursion to print the numbers from N to 1, then we need to introduce an index parameter i.
Printing N to 1 (Using Head Recursion)
"""

# Recursive function to print numbers from N to 1
def printNto1(i, n):
    if i > n:
        return
    printNto1(i+1, n)           # recursive call before printing
    print(i, end=" ")          # print after recursion call

n = 5

# Printing N to 1
printNto1(1, n)

"""

Explanation: Each recursive call increases the value of i by 1 until i becomes greater than n. On the return trip, each recursive call prints the value of i. This prints all the numbers from N to 1 using Head Recursion.

Aspect	Head Recursion	Tail Recursion
Order of Execution	Recursive calls before performing work	Work performed before recursive calls
Output (e.g., 1 to N)	Prints in reverse order (e.g., 3 2 1)	Prints in natural order (e.g., 1 2 3)
Compiler Optimization	Generally harder to optimize	Easier to optimize via tail call elimination
Typical Use Cases	Post-order tree traversals, backtracking	Loop replacements, real-time processing

"""
