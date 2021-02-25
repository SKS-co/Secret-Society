money = int(input())
num = int(input())
L = list(map(int , input().split()))
L.reverse()
s = 0
for i in range(num-1, -1):
    for i in range(num)
    if money == 0:
        break
    s += money//L[i]
    money = money%L[i]
    print("i: ", i, s ,money)

print(s)
