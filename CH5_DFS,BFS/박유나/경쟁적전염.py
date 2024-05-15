from collections import deque
graph = []
virus = []
n, k = map(int, input().split()) # 크기, 바이러스 종류
for x in range(n):
    graph.append(list(map(int, input().split())))
    for y in range(n):
        if graph[x][y] != 0: # 바이러스가 있을 경우
            virus.append((graph[x][y], 0, x, y)) # 바이러스 종류, 시간, 위치(x, y)를 우선순위 큐에 삽입
virus.sort()
virus = deque(virus)
s, s_x, s_y = map(int, input().split())
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

while virus:
    v, time, x, y = virus.popleft() # 바이러스 확산 시작
    if time == s:
        break
    for a, b in dir: # 상하좌우를 살피며
        next_x, next_y = x + a, y + b # 이동할 좌표
        if 0 <= next_x < n and 0 <= next_y < n: #시험관 범위 이내라면
            if graph[next_x][next_y] == 0: # 바이러스가 없다면
                graph[next_x][next_y] = v # 바이러스 확산
                virus.append((graph[next_x][next_y], time + 1, next_x, next_y))
print(graph[s_x - 1][s_y - 1]) # s_x, s_y 초 직전에 어떤 바이러스 였는지 반환