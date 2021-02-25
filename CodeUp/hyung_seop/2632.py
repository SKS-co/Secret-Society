n = int(input())

def stairs(num):
    if num <= 2:
        return num
    else:
        return stairs(num-1)+stairs(num-2)

result = stairs(n)
print(result)
