N, K = map(int, input().split())
m = [0 for i in range(7)]
w = [0 for i in range(7)]

for i in range(N):
    s, y = map(int, input().split())
    if s == 0: #여자
        w[y] += 1
    else:
        m[y] += 1
room = 0

for i in range(7):
    if m[i]%K != 0:
        room += 1
    if w[i]%K != 0:
        room += 1
    room += (m[i] // K)
    room += (w[i] // K)

print(room)
