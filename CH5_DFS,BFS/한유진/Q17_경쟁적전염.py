from collections import deque

N, K = map(int, input().split())
testTube = []
virusMap = []

for i in range(N):
    testTube.append(list(map(int, input().split())))
    for j in range(N):
        if testTube[i][j] != 0:
            virusMap.append((testTube[i][j], 0, i, j))
    
# 상하좌우 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

virusMap.sort()
virusQueue = deque(virusMap)

S, X, Y = map(int, input().split())

while virusQueue:
    virus, time, x, y = virusQueue.popleft()
    
    if time == S: # 시간이 되면 멈추기
        break
    
    for i in range(4): # 매초마다 모든 바이러스를 상하좌우로 퍼뜨리기
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if testTube[nx][ny] == 0:
                testTube[nx][ny] = virus
                virusQueue.append((virus, time+1, nx, ny))
                
print(testTube[X-1][Y-1])            