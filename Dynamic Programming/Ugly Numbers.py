#  Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included.

#  Given a number n, the task is to find n’th Ugly number.



def ugly_num(n):
  i2=i3=i5=0
  num=[0]*n
  num[0]=1
  

  n2=2
  n3=3
  n5=5

  for l in range(1, n):
    num[l]=min(n2,n3,n5)

    if(num[l]==n2):
      i2=i2+1
      n2=num[i2]*2
    
    if(num[l]==n3):
      i3=i3+1
      n3=num[i3]*3

    if(num[l]==n5):
      i5=i5+1
      n5=num[i5]*5
  
  print(num[n-1])

n=int(input())
ugly_num(n)
