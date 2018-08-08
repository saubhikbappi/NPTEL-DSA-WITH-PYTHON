def h(n):
    f=0
    for i in range(1,n+1):
        if (n%i)==0:
            f=f+1
    return (f%2==1)


n=36
print(h(n))


#program to find whether number is perfect square or not