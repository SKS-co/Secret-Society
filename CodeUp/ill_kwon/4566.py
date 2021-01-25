#4566
def isPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False    
  return True

sum=0  
arr=[]
m=int(input())
n=int(input())
for i in range(m,n+1):
  if(isPrime(i)):
    sum+=i
    arr.append(i)

print(sum)
print(arr[0])