import time
n, k = map(int, input().split())
#print(n, k)
L = []
L = list(map(int , input().split()))
count = 0
temp = 0
for i in range(n):
    if L[i]>k:
        continue
    
    s = L[i]
    
    if s == k:
        count+= 1
        continue
    else:
        for j in range(temp, n):# temp ~ n-1 까지의 인덱스
            s = sum(L[i:j+1])#i번째 에서 j번째까지의 합
            if s == k:
                count += 1
                temp = j
                break
            elif s > k:
                temp = j
                break
            temp = j
        if temp == n-1:
            break

print(count)
