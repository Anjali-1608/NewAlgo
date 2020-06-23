#Given 3 numbers {1, 3, 5}, we need to tell the total number of ways we can form a number 'N' using the sum of the given three numbers. 


def subp(n, count):
  if n<0:
    return 0
  if n==1:
    return 1
  if count[n]!=-1:
    return count[n]
  
  count[n]=subp(n-1, count)+subp(n-3, count)+subp(n-5, count)
  return count[n]  
  
n=int(input())
count=[-1]*(101)
subp(n, count)
