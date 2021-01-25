#4536
arr = list()
for i in range(10):
    arr.append(int(input()))

avg = sum(arr)//10
count={}
for i in arr:
    try: count[i] += 1
    except: count[i]=1
    
print(avg)
print(max(count.keys(), key=lambda k : count[k]))
