from collections import deque
N = int(input())

def bfs(ans):
    queue = deque()
    queue.append(ans)

    while True:
        n = queue.popleft()
        if n >= 2**64:
            return 0
        elif n % N == 0:
            return n
        queue.append(n*10)
        queue.append(n*10 + 1)

print(bfs(1))
