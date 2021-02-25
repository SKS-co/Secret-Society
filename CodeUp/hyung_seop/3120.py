import time
a, b = map(int, input().split())

c = b - a
count = 0
co = 10
while c != 0:
    if c > 0:
        num = (c // 10) * 10 # 가장 가까운 수
        count += (c // 10)
        c = c - num
        #print(c)
        if c == 0:
            break
            
        if 1 <= c <= 3:
            count += c
            break
        elif 4 <= c <= 7:
            c = c -5
            count += 1
        else:
            c = c - 10
            count += 1
            
    else: # C < 0
        c = abs(c)
    co += 1
    if co > 10000:
        break
print(count)
