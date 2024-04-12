def findAntennaPoint(num_house, houseLocation):
    houseLocation = sorted(houseLocation)
    print(houseLocation[(num_house - 1) // 2])

N = int(input())
houseLocation = list(map(int, input().split()))
findAntennaPoint(N, houseLocation)