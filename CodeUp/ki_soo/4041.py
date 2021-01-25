#4041

n = list(input())
n.reverse()
while True:
    i = 0
    if n[i] == '0':
        del n[i]
    else:
        break
s = 0

for i in range(len(n)):
    s = s+ int(n[i])
    print(n[i], end = '')

print('\n',end = '')
print(s)

#CLEAR
