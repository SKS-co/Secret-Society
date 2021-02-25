# 처음 배운 위상정렬 공부하자!
# 위상정렬의 핵심은 진입차수가 0인 것을 queue에 넣고
# vertex를 다 방문하기 전에 queue 가 빈다면 싸이클 발생한것!

from collections import deque
import sys

v, n = map(int, input().split())
graph = [[] for i in range(v+1)]
indegree = [0] * (v + 1) # 진입차수를 나타냄

for i in range(n):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    indegree[v2] += 1 # 각 vertex에 대한 진입차수 증가


def topology_sort(): # 위상 정렬 함수
    result = []
    queue = deque()

    for i in range(1, v+1):
        # 처음 시작하는 vertex 중 진입차수가 0인 것을 큐에 넣는다
        if indegree[i] == 0:
            queue.append(i)

    while queue: # 큐가 빌 때 까지 계속
        v1 = queue.popleft() # 큐에 담긴 vertex 하나 제거
        result.append(v1)

        for i in graph[v1]:
            indegree[i] -= 1

            if indegree[i] == 0:
                queue.append(i)
    if len(result) != v:
        print(-1)
    else:    
        for i in result:
            print(i)

topology_sort()
