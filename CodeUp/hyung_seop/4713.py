N = int(input())
L=[]
for i in range(N):
    l = list(map(int, input().split()))
    L.append(l)
dic = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10: 31, 11:30, 12:31}
i = 0
j = 0
count = 0
num = 0
for i in range(3, 12):
    num += dic[i]

fianlm = 3 #꽃이 지는 날의 월
finald = 2 #꽃이 지는 날의 일
while True:
    if (L[i][j] < fianlm) or (L[i][j] == fianlm and L[i][j+1] < finald):
        
