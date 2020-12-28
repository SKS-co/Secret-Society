#Code Up #3004
def binary_search(target, data,start, end):
    #print(start, end)
    if end < start:
        return None
    mid = (start + end) // 2
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        return binary_search(target, data, start, mid-1)
    else:
        return binary_search(target, data, mid+1, end)
    
res = 0
end = 0
n = int(input())
data =[]
data.extend(map(int, input().split()))
mod_data = [0 for i in range(len(data))]
mod_data = sorted(data)
#print(mod_data)
end = len(data)
for i in range(n):
    res = (binary_search(data[i],mod_data, 0, end))
    print(res, end = ' ')


    
