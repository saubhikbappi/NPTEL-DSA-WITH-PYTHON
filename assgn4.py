def f(m):
    if m==0:
        return (0)
    else:
        return (m+f(m-1))

m=3
print(f(m))

# terminates with factorial of a number