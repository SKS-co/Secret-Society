#0 바로 뒤에는 1만 가능 1뒤에는 1,0 가능
# 시작이 0인경우와 1인 경우를 나누자
# n==1 일때 2
def f(a,b):
  if(a==2 and b==1):
    return 2
  if(a==2 and b==0):
    return 1
  if(b==0):  
    return f(a-1,1)
  else:
    return f(a-1,0)+f(a-1,1)

n=int(input())
if(n!=1):
  print(f(n,0)+f(n,1))
else:
  print(2)