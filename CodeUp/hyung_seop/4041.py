N = int(input()) #if N = 1234
N = str(N)# 1, 2, 3, 4
#N = N.reverse()
sum = 0
count = 0
L = []
for i in range(len(N)):
    sum += int(N[i])
    #print(N[i])
    L.append(int(N[i]))
for i in range(len(L)):
    count += (10 ** i) * L[i]
#print(L)
print(count)
print(sum)
