memo = {}
def box_num(n):
    if n in memo:
        return memo[n]
    if n <=2:
        return n
    else:
        result = box_num(n-1)+box_num(n-2)
        if n not in memo:
            memo[n] = result
        return memo[n]

n = int(input())
result = box_num(n)
print(result % 100000007)
