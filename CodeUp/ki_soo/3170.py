#Code Up #3170

n, m = map(int, input().split())
data = dict()
list_data = [None for i in range(m)]
for i in range(n):
    k, v = input().split()
    v= int(v)
    if k not in data.keys():
        data[k] = v
    else:
        data[k] = data[k] + v

for i in range(m):
    list_data[i] = input()
for i in range(m):

    if list_data[i] not in data.keys():
        print('0')
    else:
        print(data[list_data[i]])
