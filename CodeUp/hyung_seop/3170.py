N, M = list(map(int, input().split(sep=' ')))
present = {}
for i in range(N):
    word, number = list(map(str, input().split(sep=' ')))
    number = int(number)
    if word in present:
        n = present[word]
        present[word] = n + number
    else:
        present[word] = number

word_L = []
for i in range(M):
    word = input()
    word_L.append(word)

for i in range(M):
    if word_L[i] in present:
        print(present[word_L[i]])
    else:
        print("0")
