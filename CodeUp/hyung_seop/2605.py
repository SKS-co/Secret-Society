nx = [0, 1, 0, -1] # 동 북 서 남
ny = [1, 0, -1, 0] # 동 북 서 남

visited = [[0 for i in range(7)] for j in range(7)]
L = []
for i in range(7):
    L.append(list(map(int, input().split())))

def dfs(x, y, answer):
    count = 0
    
    if x < 0 or x > 6 or y < 0 or y > 6:
        return False

    if visited[x][y] == 0 and L[x][y] == answer: #방문 하지 않은 행과 열
        visited[x][y] = 1
        count += 1
        
        for i in range(4):
            count += dfs(x+nx[i], y+ny[i], answer)

    return count

result = 0

for i in range(7):
    for j in range(7):
        ans = L[i][j]
        c = dfs(i, j, ans)
        if c >= 3:
            result += 1
print(result)
