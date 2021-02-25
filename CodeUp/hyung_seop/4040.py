n, m = map(int, input().split())# n : 펜션 여름 성수기 총 기간, m : 펜션이 보유하고 있는 방의 개수
L = [] # 펜션의 방을 이차원 배열로 나타냄
for i in range(n):
    l = list(input())
    L.append(l)
s, t = map(int, input().split())
N = t-s
s= s-1
count = 0
result = 0
while count < N:
    l = []
    for i in range(m):
        c = 0
        while True:
            if s+c >= n:
                break
            if L[s+c][i] == 'X':
                break
            else:
                c += 1
        l.append(c)
    num = max(l)
    if num == 0:
        result = -1
        break
    count += num
    s+=num
    if count >= N:
        break
    result += 1

print(result)

"""
이차원 배열로 팬션의 예약 배치도를 해두고
펜션에 도착하는 날을 기준으로 그때의 행부터 ox를 따져서 o가 최대로 많은 열을 고르고 count 를 함

"""
