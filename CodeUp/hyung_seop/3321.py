# 1달러 당 열량이 최대가 되는 피자
# N종류의 토핑, 같은 토핑 2개 이상 x
"""
첫 번째 줄에는 토핑 종류 수를 나타내는 하나의 정수 N (1 ≦ N ≦ 100)이 입력된다.

두 번째 줄에는 두 개의 정수 A, B (1 ≦ A ≦ 1000,1 ≦ B ≦ 1000)가 공백을 구분으로 입력된다. A는 도우의 가격, B는 토핑의 가격을 나타낸다.

세 번째 줄에는 도우의 칼로리를 나타내는 정수 C (1 ≦ C ≦ 10000)가 입력된다.

3 + i 행 (1 ≦ i ≦ N)는 i 번째의 토핑 칼로리 수를 나타내는 정수 Di (1 ≦ Di ≦ 10,000)가 입력된다.
"""


N = int(input()) # N : 토핑 종류 수
A, B = map(int, input().split()) # A : 도우의 가격, B : 토핑의 가격
C = int(input()) # 도우의 칼로리
l = []
for i in range(N):
    Di = int(input())
    l.append(Di)
l.sort()
l.reverse()

d = A # 피자의 총 가격
c = C # 피자의 총 칼로리 양
gain = c / d # 이득
newgain = 0
count = 0
while count < N:
    c += l[count]
    d += B
    newgain = c / d
    if gain < newgain :
        count += 1
        gain = newgain
        continue
    else:
        break
print(int(gain))
