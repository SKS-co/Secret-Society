K = int(input())
C = int(input())
L = []
for i in range(C):
    M, N = map(int, input().split())
    if M>N: # M이 큰 경우
        if N+(K-(M-1))>=M-1: #>= 중요
            L.append(1)
        else:
            L.append(0)

    elif N>M: # N이 큰 경우
        if  M+(K-(N-1)) > N-1: #> 중
            L.append(1)
        else:
            L.append(0)

    else: # M == N
        L.append(1)

for i in range(C):
    print(L[i])
