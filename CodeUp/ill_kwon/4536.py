#4536
from collections import Counter
sum=0
arr = [0 for i in range(10)]
i=0
while(i<10):
  arr[i]=int(input())
  sum+=arr[i]
  i+=1
cnt=Counter(arr)
mode=cnt.most_common(1)  
avr=sum/10
print(int(avr))
print(mode[0][0])