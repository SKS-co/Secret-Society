pl = [] # 파스타 리스트
jl = [] # 주스 리스트

for i in range(3):
    p = int(input())
    pl.append(p)
pl.sort()

for i in range(2):
    j = int(input())
    jl.append(j)
jl.sort()

s = pl[0] + jl[0]
s= s*1.1
print('{0:.1f}'.format(s))
