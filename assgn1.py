def g(x):
    (q,d)=(1,0)

    while q<=x:
        (q,d)=(q*10,d+1)
    return d
x=31415927

print(g(x))


#returns 8