#CodeUp #3019
#Implemented By Son
import datetime as dt
import operator
n = int(input())
default = dt.datetime.now()

schedule = [None for i in range(n)]
s_dict = dict()
for i in range(n):
    s, y, m, d = input().split()    
    schedule = dt.datetime(int(y), int(m), int(d))
    if schedule not in s_dict:
        s_dict[schedule] = s
    else:
        l = []
        l.append(s_dict[schedule])
        if type(s_dict[schedule]) is list:
            s_dict[schedule].append(s)
        else:
            s_dict[schedule] = [s_dict[schedule] , s]
        s_dict[schedule].sort()
sorted_schedule = sorted(s_dict.items(),reverse = False, key=lambda t:(t[0],t[1]))
for key, value in sorted_schedule:
    if type(value) is list:
        for i in range(len(value)):
            print(value[i])
    else:
        print(value)

