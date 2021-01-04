import copy
def merge_sort(L):
    if len(L) <= 1:
        return L
    else:
        mid = len(L)//2
        low_L = merge_sort(L[:mid])
        high_L = merge_sort(L[mid:])

    merge_L = []
    l = 0
    h = 0
    while l < len(low_L) and h < len(high_L):
        if low_L[l] > high_L[h]:
            merge_L.append(low_L[l])
            l += 1
        else:
            merge_L.append(high_L[h])
            h += 1

    merge_L += low_L[l:]
    merge_L += high_L[h:]
    return merge_L

n = int(input())
score = list(map(int, input().split()))
score_c = copy.deepcopy(score)
score_c = merge_sort(score)
grade = {}
print(score_c)
print(score)

for i in range(n):
    if i == 0:
        grade[score_c[i]] = 1
        continue
    if score_c[i] in grade:
        continue
    else:
        grade[score_c[i]] = i + 1
        
for i in score:
    print(i, grade[i])
