# Print pattern

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(j<=i):
                print(j,end="")
            else:
                print(" ",end="")
        for k in range(n-1,0,-1):
            if k<=i:
                print(k,end="")
            else:
                print(" ",end="")
        print()

pattern(int(input("Enter the value of n:")))
