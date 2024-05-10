import sys
import copy
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

#방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    queue = deque()
    #그래프 복사해오기 (2차원 깊은복사)
    test_map = copy.deepcopy(graph)
    #바이러스 위치 찾아서 큐에 넣어놓기
    for i in range(N):
        for j in range(M):
            if test_map[i][j] == 2:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]

            if (0<=nextX<N) and (0<=nextY< M):
                if test_map[nextX][nextY] == 0 :
                    test_map[nextX][nextY] = 2
                    queue.append((nextX, nextY))

    cnt = 0
    ## 0 개수를 세서 더 큰 값 answer에 넣기
    global answer
    for i in range(N):
        for j in range(M):
            if test_map[i][j] == 0:
                cnt+=1

    answer = max(answer, cnt)


def make_wall(count):
    if count == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0: #빈 공간에 벽 세우기
                graph[i][j] = 1
                make_wall(count+1)  #다시 두 번째 벽 세우러 가기
                graph[i][j] = 0    #다시 벽을 허무는 과정 (백트랙킹)

graph = [list(map(int,input().split())) for _ in range(N)]
answer = 0

make_wall(0)
print(answer)