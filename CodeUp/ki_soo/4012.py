#Code Up #4012

n = int(input())
score = []
rate = [0 for i in range(n)]
score.extend(map(int,input().split()))
rate = sorted(score)
res = dict()

for i in range(len(score)):
    if rate[i] not in res.keys():
        res[rate[i]] = n
    else:
        res[rate[i]] = n
        
    n = n -1

for i in range(len(score)):
    print(score[i], res[score[i]])

        
    
