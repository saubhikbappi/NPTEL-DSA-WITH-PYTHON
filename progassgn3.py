#Write a function sumprimes(l) that takes as input a list of integers l and retuns the sum of all the prime numbers in l.

def sumprimes(l):
    sum=0
    for i in range(0, len(l)):
        num=l[i]
        flag=0
        for j in range(2, int(num/2)+1):
            if (num % j )== 0:
                flag=1
                break
        if(flag==0 and (num!=1) and num>=0):
            sum+=num
    return sum
l=[-3,-5,3,5]
print(sumprimes(l))
