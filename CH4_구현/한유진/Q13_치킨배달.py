import itertools

def deliverChicken():
    # initial input
    N, M = map(int, input().split())
    cityInfo = []
    for i in range(N):
        cityInfo.append(list(map(int, input().split())))
    
    # find chicken store and house
    chicken_store = [(i+1, j+1) for i in range(N) for j in range(N) if cityInfo[i][j] == 2]
    house = [(i+1, j+1) for i in range(N) for j in range(N) if cityInfo[i][j] == 1]
    
    # find the minimum city's chicken distance
    chickenComb = list(itertools.combinations(chicken_store, M))

    cityChickenDistance = 1e9
    for comb in chickenComb:
        tempCCD = 0
        for r1, c1 in house:
            temp = 1e9
            for r2, c2 in comb:
                temp = min(temp, abs(r1 - r2) + abs(c1 - c2))
            tempCCD += temp
        cityChickenDistance = min(tempCCD, cityChickenDistance)
    print(cityChickenDistance)

deliverChicken()