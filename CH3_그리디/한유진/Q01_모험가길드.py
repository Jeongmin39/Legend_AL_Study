N = int(input())
fear_level = sorted(list(map(int, input().split())))
max_group = 0
group_cnt = 0


for fear in fear_level:
    group_cnt +=1
    if group_cnt >= fear:
        max_group +=1
        group_cnt = 0
        continue
print(max_group)