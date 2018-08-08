def h(m,n):
    ans=0
    while(m >= n):
        (ans , m)=(ans+1,m-n)
    return ans

m=231
n=8
print(h(m,n))

# returns 28