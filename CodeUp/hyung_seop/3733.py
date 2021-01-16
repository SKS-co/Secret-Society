import time

a, b = map(int, input().split())
memo = {}

def reculsive(memo, real, n, count):
    if n == 1:#재귀함수 종료시킴
        count += 1
        return count
    if n in memo.keys():
        #print(n, "동적")
        #print(n)
        num = memo[n]
        #print(l)
        count += num
        return count
    else:
        if n % 2 == 1:
            count = reculsive(memo, real, n*3 + 1, count)
        else: #n % 2 == 0:
            count = reculsive(memo, real, n//2, count)
        count += 1
        return count
size = []
L = []
time1 = time.time()
for i in range(a, b+1):
    count = 0
    count = reculsive(memo, i, i, count)
    L.append(count)
    #print(L)
    memo[i] = count
    #print("{}= {}".format(i, memo[i]))
time2 = time.time()
print(time2-time1)
print("끝")
#print(L)
big = max(L)
locate = L.index(big) + a
print(locate, big)
