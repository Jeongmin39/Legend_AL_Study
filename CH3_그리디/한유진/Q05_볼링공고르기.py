N, M = map(int, input().split())
balls = list(map(int, input().split()))
ballcnt = [balls.count(x) for x in range(1, M + 1)]

result = 0
for i in range(M):
    for j in range(i+1, M):
        result += ballcnt[i] * ballcnt[j]

print(result)