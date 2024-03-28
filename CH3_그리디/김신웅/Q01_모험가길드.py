n = int(input())
data = list(map(int,input().split()))
data.sort()
group_num = 0 #그룹 개수
current_num = 0  # 현재 그룹에 포함된 모험가 수

for i in range(n):
    current_num += 1  # 모험가를 그룹에 포함
    if current_num >= data[i]:  # 현재 그룹에 포함된 모험가 수가 공포도보다 크거나 같다면
        group_num += 1  # 그룹을 만들고
        current_num = 0  # 새로운 그룹을 시작함
     
print(group_num)


