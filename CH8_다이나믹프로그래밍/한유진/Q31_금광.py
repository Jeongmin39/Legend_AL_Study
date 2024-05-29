T = int(input())
maxGold = [0] * T

for i in range(T):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    
    test = [[] for _ in range(m)]
    
    for j in range(len(tmp)):
        test[j%m].append(tmp[j])
        
    first_index = 0
    last_index = m
    for j in range(m):
        maxNum = max(test[j][first_index:last_index])
        maxGold[i] += maxNum
        first_index = test[j].index(maxNum)
        
        if first_index != 0:
            first_index -= 1
            last_index = first_index + 3 if first_index + 3 <=m else m

for i in maxGold:
    print(i)