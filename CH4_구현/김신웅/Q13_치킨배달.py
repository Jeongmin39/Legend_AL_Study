import sys
from itertools import combinations

N, M = map(int, input().split())
#맵생성
arr = []
for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

#치킨집 리스트 먼저 긁어모으기 & 일반 가게 리스트 모으기
chicken = []
home_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append((i,j))
        elif arr[i][j] == 1:
            home_list.append((i,j))

#순열조합으로 뽑을 수 있는 combi 만들기
combi = list(combinations(chicken, M))

#치킨거리 계산하기 시작
chicken_distance = 99999

for com in combi:
    #가능한 M개의 치킨집 경우수의 최소거리 치킨거리 합
    temp = 0

    for home in home_list:
        chi_len = 99999 #각 집에서 한 치킨집과의 치킨 거리

        for i in range(M):
            chi_len = min(chi_len, abs(home[0]-com[i][0]) + abs(home[1]-com[i][1]))

        #각 집에서 최소 치킨거리를 더해서 보관
        temp += chi_len
    
    #combi중에서 어떤 치킨거리가 최소인지 비교해서 넣어두기
    chicken_distance = min(chicken_distance, temp)
print(chicken_distance)