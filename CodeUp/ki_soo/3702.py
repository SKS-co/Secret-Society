def pascal_tri(r, c):
    if r == 1 or c == 1:
        return 1
    else:
        return pascal_tri(r, c-1) + pascal_tri(r-1, c)

r, c = map(int, input().split())
print(pascal_tri(r,c))
