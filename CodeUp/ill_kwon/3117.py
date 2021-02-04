#3117
arr=[]
k=int(input())
i=0
while(i<k):
  temp=int(input())
  if(temp==0):
    arr.pop()
  else:  
    arr.append(temp)
  i+=1
sum=0
for i in range(len(arr)):
  sum+=arr[i]
print(sum)   

