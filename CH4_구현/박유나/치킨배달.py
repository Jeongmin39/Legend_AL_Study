from itertools import combinations

n, m = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))
result = 999999
house = []      
chicken = []      

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append([i, j])
        elif board[i][j] == 2:
            chicken.append([i, j])

for chik in combinations(chicken, m): 
    temp = 0            
    for h in house: 
        chik_len = 999
        for j in range(m):
            chik_len = min(chik_len, abs(h[0] - chik[j][0]) + abs(h[1] - chik[j][1]))
        temp = temp + chik_len
    result = min(result, temp)

print(result)