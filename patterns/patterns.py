def pattern1(n:int) ->None:
    # Write your solution here.
    for i in range(n):
        for j in range(n):
            print("*",end= " ")
        print()

def pattern2(n:int) ->None:
    # Write your solution here.
    for i in range(n):
        for j in range(i+1):
            print('*',end= " ")
        print()


def pattern3(n:int) ->None:
    # Write your solution here.
    for i in range(1,n + 1):
        for j in range(1,i + 1):
            print(j,end= " ")
        print()

def pattern4(n:int) ->None:
    # Write your solution here.
    for i in range(1,n + 1):
        for j in range(1,i + 1):
            print(i,end= " ")
        print()

def pattern5(n:int) ->None:
    # Write your solution here.
    for i in range(1,n + 1):
        for j in range((n - i) + 1):
            print("*",end= " ")
        print()

def pattern6(n:int) ->None:
    # Write your solution here.
    for i in range(1,n + 1):
        for j in range(1,((n - i) + 1) + 1):
            print(j,end= " ")
        print()

def pattern7(n:int) ->None:
    # Write your solution here.
    for i in range(n + 1):
        # space
        for j in range((n-i) + 1):
            print(" ",end="")
        
        #star
        for j in range((2*i) + 1):
            print("*",end= "")

        # space
        for j in range((n-1) + 1):
            print(" ",end="")
        print()
        
if __name__ == '__main__':
    pattern7(3)