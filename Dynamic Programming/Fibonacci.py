#   The Fibonacci numbers are the numbers in the following integer sequence.**
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

#   **Given a number n, print n-th Fibonacci Number.**


def fib(n):
   f=[-1]*n
   
   for i in range(n):
     if(i==0):
       f[i]=0
     elif(i==1):
       f[i]=1
     else:
       f[i]=f[i-1]+f[i-2]
     
   if(n<0):
       print('NIL')
   else:
       print(f)


n= int(input())

fib(n)
