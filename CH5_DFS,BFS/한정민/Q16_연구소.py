from collections import deque
import copy

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 0

def bfs():
    global answer
    queue = deque()
    temp = copy.deepcopy(graph)

    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    queue.append((nx, ny))
    count = 0
    for i in range(N):
        count += temp[i].count(0)

    answer = max(answer, count)
    
def makeWall(count):
    if count == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(count+1)
                graph[i][j] = 0

makeWall(0)
print(answer)