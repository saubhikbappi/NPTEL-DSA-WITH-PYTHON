def gcd(m,n):
    if(n>m):
        (m,n)=(n,m);
    while(m%n)!=0:
        diff=m-n
        return(gcd(max(n,diff),min(n,diff)))
    return(n)
m=72
n=16
print("The value of GCD is =",gcd(m,n))