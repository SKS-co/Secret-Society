def box_num(n):
    if n==1:
        return 2
    elif n==2:
        return 7
    elif n == 3:
        return 22
    else:
        return box_num(n-1)*2 + box_num(n-2)*3

num = int(input())
result = box_num(num)
print(result)
