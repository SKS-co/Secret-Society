import math
M, N, L = map(int , input().split())
#M : 사대의 수, N : 동물의 수, L : 사정거리
Mx = list(map(int, input().split()))
My = [0 for i in range(M)]
Nx = []
Ny = []
for i in range(N):
    x, y = map(int , input().split())
    if y > L:
        continue
    Nx.append(x)
    Ny.append(y)
#print(Mx)
count = 0
index_l=[]
for i in range(M):#사대의 수 만큼 for 문 돌면서 범위에 속하는지 체크
    a = Mx[i]
    for i in range(len(Nx)):#동물의 수만큼 돌기 만약에 속하면 del L[i]
        #print(Nx)
        b = Nx[i]
        #print("a:",a)
        #print("b: ",b)
        c = Ny[i]
        #print("c: ",c)
        L_abs = abs(a-b)+c
        if L_abs <= L:
            #print("i값", i)
            count+=1
            index_l.append(i)
    index_l.reverse()
    print(index_l)
    for i in index_l:
        #print(i,Nx[i],Ny[i])
        del Nx[i]
        del Ny[i]
    index_l.clear()


print(count)
