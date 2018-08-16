#Write a function intreverse(n) that takes as input a positive integer n and returns the integer obtained by reversing the digits in n.

#Here are some examples of how your function should work.

 #387
  #>>> intreverse(242789)
  #987242
  #>>> intreverse(3)
  #3
def interverse(n):
    rev = 0
    while (n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    return(rev)


print(interverse(4767575755545535434334343433113131333113311313131135660514442))
