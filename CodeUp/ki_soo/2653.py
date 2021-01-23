n = int(input())
arr = []
count = 0
r = 2 ** (n)

for i in range(r):
    if r == 2:
        count = 2
    arr = list('{0:b}'.format(i).zfill(n))
    for j in range(len(arr)-1):
        if arr[j] == '0' and arr[j + 1] == '0':
            break
        elif j is len(arr)-2:
            count = count + 1            
        else:
            continue
        
print(count)
