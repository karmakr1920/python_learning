"""
Approach: 
Use a for loop to iterate from 0 to N-1, where N is the number of rows. This loop will ensure to print each row of the pattern.
Inside this loop, run another loop from 0 to (N - current value of the outer loop variable). It will decrease the number of columns as the row value increases.
Now, print the asterisk in the inner loop all in one line, to complete the current row.
Move to a new line after printing each row to maintain the right-angled triangle shape of the pattern.
"""

class Solution:
    
    # Function to print pattern5
    def pattern5(self, n):
        
        # Outer loop will run for rows.
        for i in range(0,n):
            
            # Inner loop will run for columns.
            for j in range(0,n-i):
                print("*", end="")
                
            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 5

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern5(N)

if __name__ == "__main__":
    Solution().main()
