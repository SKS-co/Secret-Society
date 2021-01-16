n = int(input())
data_dict = dict()
id_list = list()
for i in range(n):
    id_num, gas = list(map(int ,input().split(sep = ' ')))
    id_list.append(id_num)
    id_list.sort()
    data_dict[id_num] = gas
for i in id_list:
    print(i , data_dict[i])