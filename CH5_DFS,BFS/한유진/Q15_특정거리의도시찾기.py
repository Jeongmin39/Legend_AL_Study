from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
result = [-1]*(N+1)
result[X] = 0
isResult = False

for citynum in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

bfs = deque()
bfs.append(X)

while bfs:
    city = bfs.popleft()
    for i in graph[city]:
        if result[i] == -1: # 아직 방문하지 않은 노드라면 최단 거리 업데이트
            result[i] = result[city] + 1 # root에서부터 부모 노드까지 거리 + 1(자식노드)
            bfs.append(i)

for i in range(N):
    if result[i+1] == K:
        print(i+1)
        isResult = True
        
if not isResult:
    print("-1")
