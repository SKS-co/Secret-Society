import math
def find_num(N):
    n = int(math.sqrt(N))
    for i in range(1, n+1):
        if i == 1:
            continue
        if N%i == 0:
            return False
    return True

M = int(input())
N = int(input())
count = 0
L = []

for i in range(M, N+1):
    if i == 1:
        continue
    if find_num(i):
        count += 1
        L.append(i)

print(sum(L))
print(min(L))
