n=int(input())

for _ in range(3):
    for i in range(1,n):
        print(" "*(n-i)+"*"*(2*i-1))