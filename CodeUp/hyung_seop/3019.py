n = int(input())
schedule = dict()
activity = []
value = []
for i in range(n):
    act, year, month, day = list(map(str, input().split(sep=' ')))
    val = int(year+month+day)
    activity.append(act)
    value.append(val)

for i in range(n-1):
    min_val = value[i]
    min_index = i
    for j in range(i ,n):
        if min_val > value[j]:
            min_val = value[j]
            min_index = j
    if min_index != i:
        activity[min_index], activity[i] = activity[i], activity[min_index]
        value[min_index], value[i] = value[i], value[min_index]

ex = 0
real = []
need = 0
for i in range(n):
    if n == 1:
        real.append(activity[i])
        break
    if i ==0:
        if value[i] == value[i+1]:
            ex = value[i]
            need =1
        else:
            need = 0
            ex = value[i]
    elif 1 <= i <= n-2:
        if need ==0:
            #real.extend(sorted(activity[len(real):i]))
            if ex == value[i]:
                need = 1
                ex = value[i]
            else:
                real.extend(sorted(activity[len(real):i]))
                need = 0
                ex = value[i]
        else: # need == 1
            if ex == value[i]:
                need = 1
                ex = value[i]
            else:
                real.extend(sorted(activity[len(real):i]))
                need = 0
                ex = value[i]
    else:#i == n - 1
        if need ==0:
            real.extend(sorted(activity[len(real):i]))
            real.append(activity[i])
        else: # need == 1
            if ex == value[i]:
                real.extend(sorted(activity[len(real):i+1]))
            else:
                real.extend(sorted(activity[len(real):i]))
                real.extend(activity[i])
for i in range(n):
    print(real[i])
        
            
