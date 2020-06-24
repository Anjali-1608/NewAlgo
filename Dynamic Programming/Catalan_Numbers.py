#   **Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems**

#    The first few Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …

#    *Time complexity of implementation is O(n2)*

def catalan(n):
  if(n==0) or (n==1):
    return 1

  cat=[0]*(n+1)
  cat[0]=1
  cat[1]=1

  for i in range(2, n+1):
    cat[i]=0 
    for j in range(i):
      cat[i]=cat[i]+cat[j]*cat[i-j-1]
  return cat[n]


n= int(input())
for i in range(n):
  print (catalan(i), end=" ")
