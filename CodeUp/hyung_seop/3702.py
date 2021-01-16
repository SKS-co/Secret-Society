row, col = map(int, input().split())
L = [[1 for i in range(col)] for j in range(row)]
#print(L)
memo = {}
def pascal(L, i, j):
    if L[i][j] != 1:
        #print("gpg")
        return L[i][j]
    if i == 0:
        return 1
    if j == 0:
        return 1
    num = pascal(L, i-1, j) + pascal(L, i, j-1)
    L[i][j] = num
    return num

num = pascal(L, row-1, col-1)
print(num % 100000000)
