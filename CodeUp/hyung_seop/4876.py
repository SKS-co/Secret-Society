N = int(input())
A = [0 for i in range(N+1)]
B = [0 for i in range(N+1)]
L_A = []
L_B = []
truth = 0
answer = []
for i in range(N):
    L_A = list(map(int, input().split()))
    for i in range(1, L_A[0]+1):
        A[L_A[i]] += 1

    L_B = list(map(int, input().split()))
    for i in range(1, L_B[0]+1):
        B[L_B[i]] += 1

    for i in range(4, 0, -1):
        if A[i] > B[i]:
            answer.append('A')
            truth = 1
            break
        elif A[i] < B[i]:
            answer.append('B')
            truth = 1
            break

    if truth == 0:
        answer.append('D')
    truth = 0
    A = [0 for i in range(5)]
    B = [0 for i in range(5)]

for i in range(N):
    print(answer[i])
