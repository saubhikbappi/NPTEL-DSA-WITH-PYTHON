def gcd(m,n):
    if(m<n):
        (m,n)=(n,m)
    if(m%n)==0:
        return(n)
    else:
        diff=m-n
        return(gcd(max(n,diff),min(n,diff)))
m=24
n=16
print("The value of GCD is =",gcd(m,n))