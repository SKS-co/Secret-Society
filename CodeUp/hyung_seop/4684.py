N = int(input())
L = list(map(int, input().split()))
max_num = N -1
i = 0
temp = 0
l = []
while i < N:
    if L[i]- L[i-1] == 1 or L[i] - L[(i +1) % 10] == - 1:
        i+=1
        continue
    if L[i] - L[i-1] == 1 or L[i] - L[(i+1)%10] == N-1:
        i+=1
        continue
    if L[i] - L[i-1] == 1-N or L[i] - L[(i+1)%10] == -1:
        i+=1
        continue

    l.append(i)
    i+=1

count = 0
ans = l[0]
if (l[0] + len(l) -1) != l[len(l)-1]: #순서가 뒤죽박죽이라면
    m = max(l)
    index = len(l)-1
    count = 1 #### 중요
    while True:
        if l[index-1] != l[index] - 1:
            break
        count += 1
    l = [i for i in range(l[0], len(l))]

    for i in range(count): #L의 위치 재조정
        temp = L.pop()
        L.insert(0, temp)

t = L[l[0]:l[len(l)-1]+1] # L 속에서 뒤집힌 부분
t.reverse() # 뒤집힌 부분 원래대로 돌리기

del L[l[0]:l[len(l)-1]+1]

for i in range(len(l)):
    L.insert(l[i], t[i])

i = L.index(1)
if i != 0:
    i = N - i

if count == 0:
    count = i%len(l)+1
    i = i - count

print(i)
print(count + ans+ 1, count + ans + len(l))
print(count)
