# 1. 첫째 줄에 테스트 케이스 T가 입력됩니다. (1 <= T <= 1000)

# 2. 매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력됩니다. (1 <= n, m <= 20)
# 둘째 줄에 n x m개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됩니다. (1 <= 각 위치에 매장된 금의 개수 <= 100)
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = []
    #좌표 넣기
    for i in range(n):
            graph.append(arr[i*m:i*m+m])

    
    #열 기준으로 위에서부터 탐색해야한다. 열은 m 
    for j in range(1, m):
        for i in range(n):
            #왼쪽위가 없다면 왼쪽과 왼쪽 아래 중 큰걸로
            if i == 0:
                graph[i][j] += max(graph[i][j-1], graph[i+1][j-1])
            #왼쪽 아래가 없다면 왼쪽위랑 왼쪽중에서 큰걸로
            elif i == n-1 :
                graph[i][j] += max(graph[i-1][j-1], graph[i][j-1])
            #다 있으면 왼쪽위, 왼쪽, 왼쪽 아래 중에서 큰걸로
            else:
                graph[i][j] += max(graph[i-1][j-1], graph[i][j-1], graph[i+1][j-1])

    result = 0
    #채굴자가 얻을 수 있는 최대 크기 비교
    for i in range(n):
        result = max(result, graph[i][m-1])
    
    print(result)
