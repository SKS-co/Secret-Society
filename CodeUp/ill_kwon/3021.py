#3021
a=list(input())
b=list(input())
if(len(a)<len(b)):
  temp=a
  a=b
  b=temp
for i in range(len(a)-len(b)):
  b.insert(0,'0')
n=len(a)
c=[]
flag=0
for i in range(len(b)):
  if(flag==0): 
    t1=a.pop()
    t2=b.pop()
    if(int(t1)+int(t2)>=10):
      t3=int(t1)+int(t2)-10
      flag=1
    else:
      t3=int(t1)+int(t2)
      flag=0
  else:
    t1=a.pop()
    t2=b.pop()
    if(int(t1)+int(t2)+1>=10):
      t3=int(t1)+int(t2)+1-10
      flag=1
    else:
      t3=int(t1)+int(t2)+1
      flag=0
  c.append(t3)
  if(flag==1 and i==n-1):
    c.append(1)
c.reverse()
for i in range(len(c)):
  print(c[i],end='')


