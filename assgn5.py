#One of the following 10 statements generates an error. Which one? (Your answer should be a number between 1 and 10.)

x=[1,"abcd",2,"efgh",[3,4]]
y=x[0:50]
print(y)
z=y
print(z)
w=x
print(w)
x[1]=x[1]+'d'
print(x)
#x[1][1]='y' TypeError: 'str' object does not support item assignment
#print(x)
y[2]=4
print(y)
z[0]=0
print(z)
w[4][0]=1000
print(w)
print(x)
a=(x[4][1]==4)
print(a)