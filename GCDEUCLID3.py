def gcd(m,n):
    for i in range(min(m,n)+1,1):
        if (m % i) == 0 and (n % i) == 0:
            mref=i
    return(i)
m=72
n=16
print("The value of GCD is =",gcd(m,n))



