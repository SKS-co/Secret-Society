def recul(n):
    if n <= 2:
        return n + 1
    else:
        return recul(n-1) + recul(n-2)

n = int(input())
result = recul(n)
print(result)
