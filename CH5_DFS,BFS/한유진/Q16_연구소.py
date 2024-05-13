N, M = map(int, input().split())
labMap = [] # 연구소 지도, 0: 빈 칸, 1: 벽, 2: 바이러스
testWall = [[0] * M for _ in range(N)]

for _ in range(N):
    labMap.append(list(map(int, input().split())))
  
dx = [0, 0, -1, 1] # 상하좌우 방향
dy = [-1, 1, 0, 0] # 상하좌우 방향

def checkVirus(x, y): # 바이러스는 상하좌우로 퍼짐
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx>=0 and nx < N and ny>=0 and ny < M:
            if testWall[nx][ny] == 0:
                testWall[nx][ny] = 2
                checkVirus(nx, ny) 
    
def checkSafeArea(): # 안전 영역은 0일 경우만 count
    safeArea = 0
    for i in range(N):
        for j in range(M):
            if testWall[i][j] == 0:
                safeArea += 1

def dfs(wall):
    global result
    
    if wall == 3: # 벽이 3개가 설치된 경우
        for i in range(N):
            for j in range(M):
                testWall[i][j] = labMap[i][j]
        
        for i in range(N):
            for j in range(M):
                if testWall[i][j] == 2:
                    checkVirus(i, j) # 바이러스 퍼진 것 확인 후
                    
        result = max(result, checkSafeArea()) # 안전 영역 크기 세기
        return
    
    for i in range(N):
        for j in range(M):
            if labMap[i][j] == 0:
                labMap[i][j] = 1
                wall += 1
                dfs(wall) # 계속해서 벽을 설치 해제하면서 안전 영역 최대 크기 찾기
                labMap[i][j] = 0
                wall -= 1
                    
dfs(0)
print(result)