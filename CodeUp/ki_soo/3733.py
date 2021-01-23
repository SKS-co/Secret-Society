class Haill(object):
    def __init__(self):
        self.leng = 1
        self.memo = {}
        
    def hail(self, n):
        print(self.memo)
        if n in [0,1]:
            return self.leng
        
        elif n in self.memo:
            self.leng = self.leng+1
            return self.memo[n]
        
        elif (n % 2) == 0:
            n = n // 2
            self.leng = self.leng +1
        
        elif (n % 2) == 1:
            n = 3 * n +1
            self.leng = self.leng +1

        self.memo[n] = self.hail(n)
        return self.memo[n]

a, b = map(int, input().split(' '))
res = [0 for i in range(2)] #index 0 is num, index 1 is length
ans = Haill()

for i in range(a, b+1):
    tmp = ans.hail(i)

    if i < res[0] and res[1] == tmp:
        continue
    elif res[1] < tmp:
        res[0] = i
        res[1] = tmp
        
print(res[0], res[1])
