L = {}
l = []
for i in range(10):
    N = int(input())
    l.append(N)
    if N in L:
        L[N] += 1
        continue
    else:
        L[N] = 1
#L = list(map(int, input().split(sep=' ')))
#print(L)
s = sum(l)
s = int(s / 10)
print(s)
l = list(L.values())
l_l = list(L.keys())
print(l_l[l.index(max(l))])
